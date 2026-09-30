from services.matching import careers, skill_gap

PROFILE={"branch":"Computer Science","interests":"data","skills":[{"name":"Python","evidence":"project"},{"name":"SQL","evidence":"self-reported"}]}
def test_multiple_explainable_careers():
    result=careers(PROFILE)
    assert len(result) >= 2
    assert "components" in result[0]
def test_gap_keeps_self_reported_distinct():
    rows=skill_gap(PROFILE,"Data Analyst")
    assert next(x for x in rows if x["Skill"] == "SQL")["Status"] == "Self-reported"
