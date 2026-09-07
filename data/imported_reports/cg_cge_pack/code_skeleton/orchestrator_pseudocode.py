"""Pseudo-orchestrator for Drop.

External side effects live here, not in CG.
"""
def cycle(campaign):
    bundle = compile_evidence(campaign)
    result = call_cg_judge(bundle)

    if result["verdict"] == "ELIGIBLE":
        return issue_launch_claim(result)

    public_feedback = redact_secret_details(result)
    proposals = call_cge_proposer(campaign, public_feedback,
                                  typed_space=load_typed_space())

    admitted = [p for p in proposals if mutation_admission_passes(p)]

    # Research actions can acquire new evidence.
    # Structural mutations create immutable child campaigns.
    return quarantine_and_schedule(admitted)
