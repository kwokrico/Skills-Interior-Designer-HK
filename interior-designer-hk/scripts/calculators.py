"""Interior design quantitative calculators for interior-designer-hk dispatcher."""

from __future__ import annotations

from typing import Any


class EgressCalculator:
    """Egress capacity and related interior metrics."""

    def calculate(self, data: dict[str, Any] | None) -> dict[str, Any]:
        if not data:
            return {"error": "data payload required"}

        calc_type = data.get("calc_type") or "egress_capacity"
        if calc_type == "egress_capacity":
            return self.egress_capacity(data)
        if calc_type == "occupancy_load":
            return self.occupancy_load(data)
        if calc_type == "thickness_buildup":
            return self.thickness_buildup(data)
        if calc_type == "lux_targeting":
            return self.lux_targeting(data)
        return {"error": f"Unknown calc_type in data: {calc_type}"}

    def egress_capacity(self, data: dict[str, Any]) -> dict[str, Any]:
        """
        Exit capacity: C = W * f (mm effective width * persons/mm factor).
        Default factor 0.6 persons/mm for stair/level per common IBC-style planning checks.
        """
        width_mm = float(data.get("clear_width_mm", 0))
        factor = float(data.get("capacity_factor", 0.6))
        occupant_load = int(data.get("occupant_load", 0))

        if width_mm <= 0:
            return {"error": "clear_width_mm must be > 0"}

        capacity = int(width_mm * factor)
        adequate = capacity >= occupant_load if occupant_load else None

        return {
            "calc_type": "egress_capacity",
            "clear_width_mm": width_mm,
            "capacity_factor": factor,
            "exit_capacity_persons": capacity,
            "required_occupant_load": occupant_load or None,
            "adequate": adequate,
            "formula": "C = W × f",
        }

    def occupancy_load(self, data: dict[str, Any]) -> dict[str, Any]:
        """
        Occupant load: OL = A / area_per_person.
        area_per_person in m² (e.g. office 9.3, assembly 0.65 seated).
        """
        area_m2 = float(data.get("area_m2", 0))
        area_per_person = float(data.get("area_per_person_m2", 9.3))

        if area_m2 <= 0 or area_per_person <= 0:
            return {"error": "area_m2 and area_per_person_m2 must be > 0"}

        load = area_m2 / area_per_person
        import math

        occupant_load = math.ceil(load)

        return {
            "calc_type": "occupancy_load",
            "area_m2": area_m2,
            "area_per_person_m2": area_per_person,
            "occupant_load": occupant_load,
            "formula": "OL = ⌈A / a_p⌉",
        }

    def thickness_buildup(self, data: dict[str, Any]) -> dict[str, Any]:
        """
        Total build-up: T_total = Σ t_i (mm).
        Flag transition when adjacent finish delta > threshold_mm (default 3).
        """
        layers = data.get("layers", [])
        adjacent_finish_mm = data.get("adjacent_finish_mm")
        threshold_mm = float(data.get("threshold_mm", 3))

        if not layers:
            return {"error": "layers list required (each with thickness_mm)"}

        thicknesses = [float(layer.get("thickness_mm", 0)) for layer in layers]
        total = sum(thicknesses)

        result: dict[str, Any] = {
            "calc_type": "thickness_buildup",
            "layers": layers,
            "total_thickness_mm": round(total, 2),
            "formula": "T_total = Σ t_i",
        }

        if adjacent_finish_mm is not None:
            delta = abs(total - float(adjacent_finish_mm))
            result["adjacent_finish_mm"] = float(adjacent_finish_mm)
            result["level_delta_mm"] = round(delta, 2)
            result["transition_detail_required"] = delta > threshold_mm
            result["threshold_mm"] = threshold_mm

        return result

    def lux_targeting(self, data: dict[str, Any]) -> dict[str, Any]:
        """Initial illuminance = maintained target / explicit overall maintenance factor."""
        import math

        if "llf" in data:
            return {"error": "Do not supply a separate llf: resolve overlapping losses into one overall maintenance_factor."}
        required = ["target_lux", "maintenance_factor"]
        fixture_fields = ["lumens_per_fixture", "room_area_m2", "utilization_factor"]
        estimate_fixtures = any(key in data for key in fixture_fields)
        if estimate_fixtures:
            required += fixture_fields
        if any(key not in data for key in required):
            return {"error": "Explicit inputs required: " + ", ".join(required)}
        try:
            values = {key: float(data[key]) for key in required}
        except (TypeError, ValueError, OverflowError):
            return {"error": "Lighting inputs must be finite positive numbers"}
        if any(isinstance(data[key], bool) or not math.isfinite(value) or value <= 0 for key, value in values.items()):
            return {"error": "Lighting inputs must be finite positive numbers"}
        if values["maintenance_factor"] > 1 or values.get("utilization_factor", 1) > 1:
            return {"error": "maintenance_factor and utilization_factor must be in (0, 1] for this estimate"}

        target_lux = values["target_lux"]
        maintenance_factor = values["maintenance_factor"]
        initial_required = target_lux / maintenance_factor

        result: dict[str, Any] = {
            "calc_type": "lux_targeting",
            "target_maintained_lux": target_lux,
            "maintenance_factor": maintenance_factor,
            "initial_design_lux": round(initial_required, 1),
            "formula": "E_initial = E_maintained / MF_total",
            "basis": "maintenance_factor is the overall non-overlapping factor; estimate only, not photometric or compliance validation",
        }

        if estimate_fixtures:
            lumens_per_fixture = values["lumens_per_fixture"]
            room_area_m2 = values["room_area_m2"]
            utilization_factor = values["utilization_factor"]
            total_lumens_needed = (initial_required * room_area_m2) / utilization_factor
            fixture_count = math.ceil(total_lumens_needed / lumens_per_fixture)
            result["room_area_m2"] = room_area_m2
            result["utilization_factor"] = utilization_factor
            result["lumens_per_fixture"] = lumens_per_fixture
            result["estimated_fixture_count"] = fixture_count

        return result
