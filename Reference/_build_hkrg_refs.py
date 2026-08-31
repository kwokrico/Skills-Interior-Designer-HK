"""One-off builder: generate HKRG reference markdown from _hkrg-extract.txt."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXTRACT = ROOT / "_hkrg-extract.txt"
SITE = ROOT.parent / "interior-designer-hk" / "subskills" / "interior-site-supervision" / "references"
HANDOVER = ROOT.parent / "interior-designer-hk" / "subskills" / "interior-handover-dlp" / "references"
TENDER = ROOT.parent / "interior-designer-hk" / "subskills" / "interior-tendering-qa" / "references"


def clean(s: str) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    return s


def load_pages() -> dict[int, str]:
    text = EXTRACT.read_text(encoding="utf-8")
    pages: dict[int, str] = {}
    for m in re.finditer(r"===== PAGE (\d+) =====\n(.*?)(?=\n===== PAGE |\Z)", text, re.S):
        pages[int(m.group(1))] = m.group(2)
    return pages


def join_pages(pages: dict[int, str], start: int, end: int) -> str:
    return "\n".join(pages.get(i, "") for i in range(start, end + 1))


def extract_numbered_items(block: str) -> list[str]:
    items = []
    for line in block.splitlines():
        line = clean(line)
        if re.match(r"^\d+\.$", line):
            continue
        m = re.match(r"^(\d+)\.\s*(.*)", line)
        if m and m.group(2):
            items.append(clean(m.group(2)))
        elif m and not m.group(2):
            continue
        elif line and not line.startswith("（") and "香港裝修指引" not in line:
            if items and not re.match(r"^\d+\.", line) and len(line) > 8:
                # continuation of previous item
                items[-1] = clean(items[-1] + " " + line)
    return [i for i in items if len(i) > 3]


def section_from_pages(pages: dict[int, str], page_start: int, page_end: int, header: str) -> str:
    block = join_pages(pages, page_start, page_end)
    lines = []
    lines.append(f"## {header}\n")
    lines.append(f"Source: `HKRG §裝修需知/{header.split()[0]}`, PDF ~p.{page_start}–{page_end}\n")
    current = None
    general: list[str] = []
    extra: list[str] = []
    mode = "general"
    for raw in block.splitlines():
        line = clean(raw)
        if not line or "香港裝修指引" in line or re.match(r"^（07/2022）", line):
            continue
        if line in ("一般需知", "另收費項目"):
            mode = "general" if "一般" in line else "extra"
            continue
        if re.match(r"^1\.\d+", line) and header not in line:
            continue
        m = re.match(r"^(\d+)\.\s*(.+)", line)
        if m:
            txt = clean(m.group(2))
            if mode == "general":
                general.append(txt)
            else:
                extra.append(txt)
        elif line.startswith("除非報價單"):
            extra.append(line)
    if general:
        lines.append("### 一般需知 (General)\n")
        for i, t in enumerate(general, 1):
            lines.append(f"{i}. {t}")
        lines.append("")
    if extra:
        lines.append("### 另收費項目 (Extra charge triggers)\n")
        for i, t in enumerate(extra, 1):
            lines.append(f"{i}. {t}")
        lines.append("")
    return "\n".join(lines)


def build_part1_trades(pages: dict[int, str]) -> str:
    sections = [
        ("1.1 工程整體", 12, 13),
        ("1.2 客方第三方供應商的度尺、送貨、安裝", 14, 14),
        ("1.3 清拆工程", 15, 15),
        ("1.4 水電工程", 16, 17),
        ("1.5 煤氣工程", 18, 18),
        ("1.6 鋁窗工程", 19, 19),
        ("1.7 防水工程", 20, 20),
        ("1.8 泥水工程", 21, 22),
        ("1.9 訂造傢俬", 23, 24),
        ("1.10 油漆 / 牆紙", 25, 26),
        ("1.11 木門", 27, 27),
        ("1.12 木地板", 28, 28),
        ("1.13 假天花", 29, 29),
        ("1.14 清潔及保養", 30, 31),
    ]
    out = [
        "# HKRG — 裝修需知 (by trade)\n",
        "Source: `HKRG §裝修需知/1.2–1.14`, PDF ~p.12–31. Industry practice only.\n",
    ]
    for hdr, ps, pe in sections:
        out.append(section_from_pages(pages, ps, pe, hdr))
    return "\n".join(out)


def build_part1_overall(pages: dict[int, str]) -> str:
    return """# HKRG — 裝修需知 (overview)

Source: `HKRG §裝修需知`, PDF ~p.8–31. Published by HKAS, HKBIA, Codeco (好師傅). **裝修資訊** on HKAS website = same document family.

## Purpose

Fair, transparent client (客方) ↔ contractor (承辦方) collaboration for Hong Kong residential renovation. Reduces expectation gaps and disputes. **Not statutory law** — verify BD/FSD/EMSD/WSD/LD and estate rules.

## Document parts

| Part | Name | Skill owner |
|------|------|-------------|
| 1 | 裝修需知 | `interior-site-supervision` |
| 2 | 驗收指引 (自助驗收) | `interior-handover-dlp` |
| 3 | 標準報價單 | `interior-tendering-qa` |

## Contract adoption (boilerplate)

> 本工程將採用《香港裝修指引》中的「裝修需知」及「驗收指引」，作為工作流程與驗收的標準。

(Also embedded as clause 23 in standard quotation T&C — see `hkrg-standard-quotation-contract.md`.)

## HKRG vs HKEDCA (when to load which)

| Topic | Primary | Secondary |
|-------|---------|-----------|
| Trade sequence, site protection, BOQ measurement | HKEDCA | HKRG Part 1 client duties |
| Quote, payment, variations, DLP in contract | HKRG Part 3 | HKEDCA standard contract scope |
| Owner snag checklist | HKRG Part 2 | HKEDCA §交收 cleaning & methods |
| Technical waterproof/MEP depths | HKEDCA | HKRG high-level only |

## Cross-trade rules (from §1.1 工程整體)

""" + "\n".join(
        f"{i}. {t}"
        for i, t in enumerate(
            extract_numbered_items(join_pages(pages, 12, 13)),
            1,
        )
    )


def build_part2(pages: dict[int, str]) -> str:
    sections = [
        ("2.1 來去水接駁系統 / 地台去水", 34, 34),
        ("2.2 潔具", 34, 35),
        ("2.3 電工", 35, 37),
        ("2.4 門 / 窗 / 玻璃及鏡 / 露台", 37, 38),
        ("2.5 鋪磚 （地台及牆身）", 39, 39),
        ("2.6 地面批盪 / 牆身批盪", 40, 40),
        ("2.7 傢俬", 41, 41),
        ("2.8 廚櫃", 42, 42),
        ("2.9 油漆", 43, 43),
        ("2.10 牆紙", 43, 43),
        ("2.11 木工", 44, 44),
        ("2.12 木地板", 45, 45),
        ("2.13 電器 / 智能家電 / 燈", 46, 46),
        ("2.14 冷氣安裝", 46, 46),
        ("2.15 清潔", 46, 47),
    ]
    out = [
        "# HKRG — 驗收指引 (自助驗收)\n",
        "Source: `HKRG §驗收指引`, PDF ~p.33–47. Checklist for non-specialist handover walk. Reasonable contractor standard.\n",
        "| HKRG method | Typical test | HKEDCA cross-ref |\n",
        "|-------------|--------------|------------------|\n",
        "| Visual 目測 | Finishes, alignment | HKEDCA §交收/5 目測 |\n",
        "| Sound 耳聽 | Hollow plaster | HKEDCA §交收/5 耳聽 |\n",
        "| Foot 腳踏 | Timber floor | HKEDCA §交收/5 腳踏 |\n",
        "| Level 平水尺 | Slopes, frames | HKEDCA §交收/5 平水尺 |\n",
        "| Water 灑水 | Wet areas, windows | HKEDCA §交收/5 灑水 (management approval) |\n",
        "\n",
    ]
    for hdr, ps, pe in sections:
        block = join_pages(pages, ps, pe)
        out.append(f"## {hdr}\n")
        out.append(f"Source: `HKRG §驗收指引/{hdr.split()[0]}`, PDF ~p.{ps}–{pe}\n")
        items: list[str] = []
        for raw in block.splitlines():
            line = clean(raw)
            if not line or "香港裝修指引" in line or re.match(r"^（07/2022）", line):
                continue
            if re.match(r"^2\.\d+", line):
                continue
            if line in ("門", "窗", "電線", "電掣 / 開關掣位 / 電燈", "配電箱", "玻璃及鏡", "露台",
                        "地面批盪", "牆身及天花批盪", "木天花 、 木燈槽 、 木殼柱 、 木橫樑等", "木器裝飾"):
                continue
            m = re.match(r"^(\d+)\.\s*(.+)", line)
            if m:
                items.append(clean(m.group(2)))
            elif items and len(line) > 5 and not re.match(r"^\d+\.$", line):
                items[-1] = clean(items[-1] + " " + line)
        for i, t in enumerate(items, 1):
            out.append(f"{i}. {t}")
        out.append("")
    return "\n".join(out)


def build_part3(pages: dict[int, str]) -> str:
    terms = join_pages(pages, 54, 55)
    clause_items = []
    in_terms = False
    for raw in terms.splitlines():
        line = clean(raw)
        if "條款及細則" in line:
            in_terms = True
            continue
        if not in_terms:
            continue
        if line.startswith("付款安排"):
            break
        m = re.match(r"^(\d+)\.\s*(.+)", line)
        if m:
            clause_items.append((int(m.group(1)), clean(m.group(2))))
        elif clause_items and line and not line.startswith("（"):
            n, t = clause_items[-1]
            clause_items[-1] = (n, clean(t + " " + line))

    out = [
        "# HKRG — 標準報價單 & 條款及細則\n",
        "Source: `HKRG §標準報價單`, PDF ~p.49–58; sample ~p.59–66; 保留清單 ~p.69–71.\n",
        "**Template only — legal review required.**\n",
        "## BOQ section structure (blank template)\n",
        "| § | Trade section | HKEDCA BOQ map |\n",
        "|---|---------------|----------------|\n",
        "| 1 | 清拆工程 | HKEDCA §清拆 |\n",
        "| 2 | 水電工程 | HKEDCA §水電 |\n",
        "| 3 | 泥水工程 | HKEDCA §坭水/防水 |\n",
        "| 4 | 木工工程 | HKEDCA §木工前期+後期 |\n",
        "| 5 | 油漆工程 | HKEDCA §油漆 |\n",
        "| 6 | 外牆工程 | Aluminium/scaffold (HKEDCA pre-start) |\n",
        "| 7 | 代客安裝服務 | Owner-supplied install |\n",
        "| 8 | 前期及其他項目 | Protection, temp lights, site waste |\n",
        "| 9 | 工程保險 | Third-party + employees compensation |\n",
        "\n",
        "## Header fields\n",
        "- 承辦方 / 客方: name, phone, email, site address; contractor company, address, responsible person\n",
        "- 開工日期 / 完工日期\n",
        "- 合共港幣 / 折扣 / 折實港幣\n",
        "\n",
        "## Payment schedule (template)\n",
        "| Stage | % slot | Typical sample (PDF p.65) |\n",
        "|-------|--------|---------------------------|\n",
        "| 細訂 | ___% | 10% on signing |\n",
        "| 大訂 | ___% | 30% before start |\n",
        "| 二期 | ___% | 15% after MEP complete |\n",
        "| 三期 | ___% | 15% after masonry complete |\n",
        "| 四期 | ___% | 20% after joinery delivered & installed |\n",
        "| 尾期 | ___% | 10% after completion & snag (clause 10) |\n",
        "\n",
        "## 條款及細則 (full text, clauses 1–24)\n",
    ]
    for n, t in clause_items:
        out.append(f"### Clause {n}\n\n{t}\n")
    out.append("""
## Clause 23 — HKRG adoption (verbatim)

本工程將採用《香港裝修指引》中的「裝修需知」及「驗收指引」，作為工作流程與驗收的標準。

## Tender QA — completeness checks

| Risk | Check |
|------|-------|
| Missing insurance line | §9 third-party + labour; scaffold scope stated |
| Owner-supply items | Clause 4 — tiles, appliances, locks listed |
| Completion definition | Clause 10 — reasonable occupation; snag holdback clause 10 |
| Variations | Clause 14 — written VO before work |
| DLP | Clause 12 — months blank; 3-month repair window from notice |
| LD / delay damages | Optional daily sum at payment section |
| Dispute | HKAS mediation → arbitration; Hong Kong law |
| Retention list | Attachment §5 — signed before demolition |

## Sample line items (reference only)

See PDF pp.60–64 for illustrative quantities (清拆 1.1–1.8, 水電 2.1–2.7, 泥水 3.1–3.10, 木工 4.1–4.16, 油漆 5.1–5.4, 外牆 6.1–6.4, 代客安裝 7.1–7.8, 前期 8.1–8.4).

## Attachment — 保留清單 (Retention list)

Source: `HKRG §附件/保留清單`, PDF ~p.70–71.

- 全部物件不需要保留：是 / 否
- Rooms: 客飯廳, 廚房, 廁所, 主人房, 客房1, 客房2, 工人房/儲物室
- Per room: tick 冷氣機, 窗台石, 門及框, 天花燈, 廚櫃, 潔具, 窗簾, etc. (see PDF)
- Align with `HKRG §裝修需知/1.3` — client completes before demolition
""")
    return "\n".join(out)


def build_index() -> str:
    return """# HKRG Index — 香港裝修指引 (平台版 2.0)

## Document metadata

| Field | Value |
|-------|-------|
| Title | 香港裝修指引 (Hong Kong Renovation Guidelines) |
| Web name | 裝修資訊 (Renovation Information) — [HKAS](https://www.hkarbsoc.org.hk/hk/renovation_hk.htm) |
| Publishers | 香港仲裁公會 (HKAS), 香港樓宇檢驗學會 (HKBIA), 好師傅 (Codeco) |
| Canonical file | [HKRG-香港裝修指引-2.0.pdf](HKRG-香港裝修指引-2.0.pdf) |
| Version | 2.0 (07/2022 print) |
| Language | Traditional Chinese (source); English structure in sub-skill `references/` |
| Approx. length | 74 PDF pages |

## Disclaimer

Voluntary **industry practice**, not statutory law. Do not replace legal advice. User bears risk of reliance. Always verify:

- Buildings Department (BD), Fire Services Department (FSD), Labour Department (LD)
- EMSD, WSD, estate / owners' corporation, insurance, project contract

## Citation format

`HKRG §{part}/{section}` — e.g. `HKRG §驗收指引/2.5`, `HKRG §標準報價單/條款14`, `HKRG §裝修需知/1.4`.

Markdown extracts: `interior-designer-hk/subskills/{skill_id}/references/hkrg-*.md`.

## Table of contents (PDF page anchors)

| Section | PDF pages (approx.) | Sub-sections |
|---------|---------------------|--------------|
| 免責聲明 | 4 | — |
| 序 | 8–9 | Purpose, three parts |
| **1. 裝修需知** | 11–31 | 1.1–1.14 (see below) |
| **2. 驗收指引** | 33–47 | 2.1–2.15 |
| **3. 標準報價單** | 49–58 | Blank template + T&C clauses 1–24 |
| **4. 標準報價單（樣本）** | 59–66 | Worked example |
| **5. 附件：保留清單** | 69–71 | Pre-demolition retention form |

### Part 1 — 裝修需知 (doc pp. 02–20)

| § | Topic | PDF ~p. |
|---|-------|---------|
| 1.1 | 工程整體 | 12–13 |
| 1.2 | 客方第三方度尺/送貨/安裝 | 14 |
| 1.3 | 清拆工程 | 15 |
| 1.4 | 水電工程 | 16–17 |
| 1.5 | 煤氣工程 | 18 |
| 1.6 | 鋁窗工程 | 19 |
| 1.7 | 防水工程 | 20 |
| 1.8 | 泥水工程 | 21–22 |
| 1.9 | 訂造傢俬 | 23–24 |
| 1.10 | 油漆/牆紙 | 25–26 |
| 1.11 | 木門 | 27 |
| 1.12 | 木地板 | 28 |
| 1.13 | 假天花 | 29 |
| 1.14 | 清潔及保養 | 30–31 |

### Part 2 — 驗收指引 (doc pp. 24–37)

| § | Topic | PDF ~p. |
|---|-------|---------|
| 2.1–2.2 | 來去水/潔具 | 34–35 |
| 2.3 | 電工 | 35–37 |
| 2.4 | 門窗玻璃露台 | 37–38 |
| 2.5–2.6 | 鋪磚/批盪 | 39–40 |
| 2.7–2.8 | 傢俬/廚櫃 | 41–42 |
| 2.9–2.10 | 油漆/牆紙 | 43 |
| 2.11–2.12 | 木工/木地板 | 44–45 |
| 2.13–2.15 | 電器/冷氣/清潔 | 46–47 |

## Skill routing table

| HKRG part | `skill_id` | Reference file(s) |
|-----------|------------|-------------------|
| 裝修需知 (overview + 1.1) | `interior-site-supervision` | `hkrg-renovation-essentials.md` |
| 裝修需知 (1.2–1.14 trades) | `interior-site-supervision` | `hkrg-renovation-essentials-trades.md` |
| 驗收指引 | `interior-handover-dlp` | `hkrg-self-inspection-handover.md` |
| 標準報價單 + 保留清單 | `interior-tendering-qa` | `hkrg-standard-quotation-contract.md` |
| 額外工程費 / VE triggers | `interior-value-engineering` | `hkrg-renovation-essentials-trades.md` (另收費) |
| Pre-start (client view) | `interior-statutory-compliance` | `hkrg-renovation-essentials-trades.md` §1.3 |

## HKRG vs HKEDCA

| | HKRG | HKEDCA |
|---|------|--------|
| Audience | Homeowner + contractor | Trade contractor / 判頭 |
| Strength | Contract, payment, owner acceptance | Sequence, protection, measurement |
| Handover | Room checklist (Part 2) | Cleaning sequence, trade tests (§交收) |
| Contract | Standard quotation (Part 3) | 室內工程標準合同 |

Use **both** for HK residential: HKRG for client contract & snag; HKEDCA for site execution & BOQ.

## Contract adoption boilerplate

本工程將採用「裝修資訊」中的「裝修需知」及「自助驗收指引」，作為工作流程與驗收的標準。

(Part 3 template uses 《香港裝修指引》 wording for 「裝修需知」及「驗收指引」.)

## Glossary

| Term | English | Notes |
|------|---------|-------|
| 客方 | Client / owner | Pays, supplies owner materials |
| 承辦方 | Contractor | Executes works per quotation |
| 裝修資訊 | Renovation Information | HKAS web branding |
| 驗收指引 | Acceptance guide | Part 2; aka 自助驗收 on web |
| 執漏 | Snag rectification | May be post-handover per §1.1 |
| 變更工程 | Variation works | Clause 14 |
| 交吉 | Vacant possession | Clause 1 — before start |

## Extraction status

| Reference file | Status |
|----------------|--------|
| `hkrg-renovation-essentials.md` | Integrated v1 (2026-05) |
| `hkrg-renovation-essentials-trades.md` | Integrated v1 (2026-05) |
| `hkrg-self-inspection-handover.md` | Integrated v1 (2026-05) |
| `hkrg-standard-quotation-contract.md` | Integrated v1 (2026-05) |

## Master skill pointer

Dual-source HK routing: [interior-designer-hk/SKILL.md](../interior-designer-hk/SKILL.md) §1.10 (HKEDCA) + §1.11 (HKRG).
"""


def main():
    pages = load_pages()
    SITE.mkdir(parents=True, exist_ok=True)
    HANDOVER.mkdir(parents=True, exist_ok=True)
    TENDER.mkdir(parents=True, exist_ok=True)

    (ROOT / "HKRG-INDEX.md").write_text(build_index(), encoding="utf-8")
    (SITE / "hkrg-renovation-essentials.md").write_text(build_part1_overall(pages), encoding="utf-8")
    (SITE / "hkrg-renovation-essentials-trades.md").write_text(build_part1_trades(pages), encoding="utf-8")
    (HANDOVER / "hkrg-self-inspection-handover.md").write_text(build_part2(pages), encoding="utf-8")
    (TENDER / "hkrg-standard-quotation-contract.md").write_text(build_part3(pages), encoding="utf-8")
    print("Wrote HKRG-INDEX + 4 reference files")


if __name__ == "__main__":
    main()