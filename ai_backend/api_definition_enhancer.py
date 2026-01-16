from ai_backend.api_definition_enhancer import enhance_definition_with_api
def rewrite_definition(line):
    if "east india company" in line.lower():
        base_definition = (
            "• East India Company (EIC) was a British trading company "
            "established in 1600 to conduct trade with India and the East."
        )
        return enhance_definition_with_api(base_definition)

    return enhance_definition_with_api("• " + line.capitalize())
