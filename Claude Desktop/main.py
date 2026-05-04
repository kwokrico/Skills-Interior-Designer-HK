import os
import json
import sys

# Specialized math logic can still reside in /core
try:
    from core.calculators import EgressCalculator
except ImportError:
    EgressCalculator = None


class InteriorDesignerDispatcher:
    def __init__(self):
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.sub_skills_base = os.path.join(self.base_path, "sub_skills")

        # Mapping Skill IDs to their specific folders
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
            "interior-sustainability-wellness"
        ]

    def load_sub_skill(self, skill_id):
        """Navigates to sub_skills/{id}/{id}.md and returns content."""
        if skill_id not in self.valid_skills:
            return {"error": f"Skill ID '{skill_id}' not recognized."}

        # New Path Logic: Look inside the sub-folder for the .md file
        file_path = os.path.join(self.sub_skills_base, skill_id, f"{skill_id}.md")
        ref_path = os.path.join(self.sub_skills_base, skill_id, "references")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # List available reference files so Claude knows what else it can ask to see
            available_refs = []
            if os.path.exists(ref_path):
                available_refs = os.listdir(ref_path)

            return {
                "status": "success",
                "skill_id": skill_id,
                "instructions": content,
                "references_available": available_refs
            }
        except FileNotFoundError:
            return {"error": f"Expected file at {file_path} not found."}
        except Exception as e:
            return {"error": str(e)}

    def run_interior_calculator(self, calc_type, data=None):
        """Pure mathematical routing for interior design metrics."""
        if calc_type == "egress_capacity":
            if not EgressCalculator:
                return {"error": "Egress module not found in /core."}
            calc = EgressCalculator()
            result = calc.calculate(data)
            return {"status": "success", "result": result}

        elif calc_type == "occupancy_load":
            return {"status": "success", "msg": "Occupancy load calculation logic ready."}

        elif calc_type == "thickness_buildup":
            return {"status": "success", "msg": "Thickness build-up calculation logic ready."}

        elif calc_type == "lux_targeting":
            return {"status": "success", "msg": "Lighting lux targeting logic ready."}

        return {"error": f"Calculator '{calc_type}' not recognized."}


def main():
    try:
        # Standard input for Claude Desktop Skills
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
                arguments.get("data")
            )
        else:
            result = {"error": f"Unknown tool: {tool_name}"}

        sys.stdout.write(json.dumps(result))

    except Exception as e:
        sys.stdout.write(json.dumps({"error": f"Dispatcher Error: {str(e)}"}))


if __name__ == "__main__":
    main()