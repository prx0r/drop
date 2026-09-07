from __future__ import annotations


def spin_manifest(frame_urls: list[str], *, lazy: bool = True) -> dict:
    """Create a deployment manifest for a truth-preserving 360 spin.

    Frames should be real supplier/sample photographs of the exact SKU. Generative
    interpolation is intentionally not used for factual 360 product inspection.
    """
    if len(frame_urls) < 8:
        raise ValueError("at least 8 real product frames are required for a useful 360 spin")
    return {
        "provider": "sirv-compatible",
        "frame_count": len(frame_urls),
        "frames": frame_urls,
        "initialize_on": "click" if lazy else "load",
        "qa": [
            "all frames depict the exact sellable SKU",
            "sequence covers one continuous rotation",
            "no generative geometry edits",
            "verify logos, ports, controls and included accessories",
        ],
    }
