import re


SECTION_PATTERNS = [

    r"3\.1 Release Details",

    r"3\.2 Application Details",

    r"3\.3 System Requirements",

    r"3\.4 Delivered EPICs",

    r"3\.4 Delivered Services",

    r"3\.5 Delivered EPICs",

    r"3\.6 Static Code Analysis SonarQube",

    r"3\.7 Known / Open Issues",

    r"4 Deliverables",

    r"5\. Risks",

    r"6\. Post Installation Verification",

    r"7\. Contact Information"

]


def split_into_sections(text):

    matches = []

    for pattern in SECTION_PATTERNS:

        for match in re.finditer(
            pattern,
            text,
            re.IGNORECASE
        ):

            matches.append(
                (
                    match.start(),
                    match.group()
                )
            )

    matches.sort()

    sections = []

    for i in range(len(matches)):

        start = matches[i][0]
        title = matches[i][1]

        if i < len(matches) - 1:
            end = matches[i + 1][0]
        else:
            end = len(text)

        section_content = text[start:end]

        sections.append({
            "section": title,
            "content": section_content
        })

    return sections