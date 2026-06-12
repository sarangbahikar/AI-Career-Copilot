from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def create_report(
    filename,
    score,
    skills,
    roles,
    roadmap
):

    doc = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Career Copilot Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            f"ATS Score: {score}/100",
            styles["Heading2"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    content.append(
        Paragraph(
            "Detected Skills",
            styles["Heading2"]
        )
    )

    for skill in skills:

        content.append(
            Paragraph(
                f"• {skill}",
                styles["Normal"]
            )
        )

    content.append(
        Spacer(1, 10)
    )

    content.append(
        Paragraph(
            "Recommended Roles",
            styles["Heading2"]
        )
    )

    for role in roles:

        content.append(
            Paragraph(
                f"• {role}",
                styles["Normal"]
            )
        )

    content.append(
        Spacer(1, 10)
    )

    content.append(
        Paragraph(
            "Learning Roadmap",
            styles["Heading2"]
        )
    )

    for step in roadmap:

        content.append(
            Paragraph(
                f"• {step}",
                styles["Normal"]
            )
        )

    doc.build(content)