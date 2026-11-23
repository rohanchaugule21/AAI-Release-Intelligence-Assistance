import json
from pathlib import Path

ROOT = Path(
    r"C:\Users\Rohan.Chaugule\Documents\Github\ReleaseIntelligence"
)

COMPONENT_FILE = (
    ROOT / "data" / "component_master.json"
)

with open(
    COMPONENT_FILE,
    "r",
    encoding="utf-8"
) as fp:

    COMPONENTS = json.load(fp)


def compare_components(
    release1,
    release2
):

    release1_components = [

        component

        for component in COMPONENTS

        if component["release_number"]
        == release1
    ]

    release2_components = [

        component

        for component in COMPONENTS

        if component["release_number"]
        == release2
    ]

    common = []

    r1_names = {
        c["component_name"]
        for c in release1_components
    }

    r2_names = {
        c["component_name"]
        for c in release2_components
    }

    for name in sorted(
        r1_names.intersection(
            r2_names
        )
    ):

        common.append(name)

    return {

        "release_1": release1,

        "release_2": release2,

        "present_in_release_1":
            release1_components,

        "present_in_release_2":
            release2_components,

        "common":
            common
    }