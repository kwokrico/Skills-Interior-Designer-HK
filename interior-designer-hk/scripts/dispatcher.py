import os
import json
import sys

try:
    from calculators import EgressCalculator
except ImportError:
    EgressCalculator = None


class InteriorDesignerDispatcher:
    def __init__(self):
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.subskills_base = os.path.join(self.base_path, "subskills")

        self.valid_skills = [
            "interior-fire-life-safety",
            "interior-mep-clash-detection",
            "interior-statutory-compliance",
            "interior-acoustic-engineering",
            "interior-material-procurement",
            "interior-interface-detailing",
            "interior-thickness-build-up",
            "interior-millwork-technical",
            "interior-value-engineering",
            "interior-tendering-qa",
            "interior-site-supervision",
            "interior-handover-dlp",
            "interior-anthropometrics-ergonomics",
            "interior-lighting-science",
            "interior-brand-environmental-graphics",
            "interior-sustainability-wellness",
        ]

    def load_sub_skill(self, skill_id):
        """Navigates to subskills/{id}/{id}.md and returns content."""
        if skill_id not in self.valid_skills:
            return {"error": f"Skill ID '{skill_id}' not recognized."}

        file_path = os.path.join(self.subskills_base, skill_id, f"{skill_id}.md")
        ref_path = os.path.join(self.subskills_base, skill_id, "references")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            available_refs = []
            if os.path.exists(ref_path):
                available_refs = os.listdir(ref_path)

            return {
                "status": "success",
                "skill_id": skill_id,
                "instructions": content,
                "references_available": available_refs,
            }
        except FileNotFoundError:
            return {"error": f"Expected file at {file_path} not found."}
        except Exception as e:
            return {"error": str(e)}

    def run_interior_calculator(self, calc_type, data=None):
        """Pure mathematical routing for interior design metrics."""
        if not EgressCalculator:
            return {"error": "Calculator module not found in scripts/."}

        valid_types = (
            "egress_capacity",
            "occupancy_load",
            "thickness_buildup",
            "lux_targeting",
        )
        if calc_type not in valid_types:
            return {"error": f"Calculator '{calc_type}' not recognized."}

        payload = dict(data or {})
        payload["calc_type"] = calc_type
        calc = EgressCalculator()
        result = calc.calculate(payload)
        if "error" in result:
            return {"status": "error", "result": result}
        return {"status": "success", "result": result}


def main():
    try:
        raw_input = sys.stdin.read()
        if not raw_input:
            return

        input_data = json.loads(raw_input)
        tool_name = input_data.get("tool")
        arguments = input_data.get("arguments", {})

        dispatcher = InteriorDesignerDispatcher()

        if tool_name == "load_sub_skill":
            result = dispatcher.load_sub_skill(arguments.get("skill_id"))
        elif tool_name == "run_interior_calculator":
            result = dispatcher.run_interior_calculator(
                arguments.get("calc_type"),
                arguments.get("data"),
            )
        else:
            result = {"error": f"Unknown tool: {tool_name}"}

        sys.stdout.write(json.dumps(result))

    except Exception as e:
        sys.stdout.write(json.dumps({"error": f"Dispatcher Error: {str(e)}"}))


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "load":
        dispatcher = InteriorDesignerDispatcher()
        sys.stdout.write(json.dumps(dispatcher.load_sub_skill(sys.argv[2])))
    else:
        main()
