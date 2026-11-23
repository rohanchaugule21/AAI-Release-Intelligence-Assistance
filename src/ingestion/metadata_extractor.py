import re


def extract_release_number(filename):
    """
    Extract release number from filenames like:

    AAI IRS ReleaseNoteV6.0.0.0.docx
    AAI IRS ReleaseNoteV4.0.0.0 1.docx
    AAI IRS ReleaseNoteV23.0.0.docx

    Returns:
        6
        4
        23
    """

    match = re.search(
        r"ReleaseNoteV(\d+)",
        filename,
        re.IGNORECASE
    )

    if match:
        return int(match.group(1))

    return None


def extract_release_version(filename):
    """
    Extract full version.

    Examples:

    V6.0.0.0
    V23.0.0
    """

    match = re.search(
        r"(V\d+(?:\.\d+)*)",
        filename,
        re.IGNORECASE
    )

    if match:
        return match.group(1)

    return None


def extract_airport(folder_path):

    path = folder_path.upper()

    if "AAI22" in path:
        return "AAI22"

    if "AAI44" in path:
        return "AAI44"

    return "UNKNOWN"