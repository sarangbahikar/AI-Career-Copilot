def get_recommendations(weaknesses):

    recommendations = []

    for weakness in weaknesses:

        if "GitHub" in weakness:
            recommendations.append(
                "Add GitHub profile link"
            )

        elif "LinkedIn" in weakness:
            recommendations.append(
                "Add LinkedIn profile link"
            )

        elif "Certification" in weakness:
            recommendations.append(
                "Add industry certifications"
            )

        elif "Portfolio" in weakness:
            recommendations.append(
                "Create a portfolio website"
            )

    return recommendations