import json

DEBUG = False
if DEBUG:
    from config import PATH
    from pprint import pprint


def load_candidates_from_json(path):
    with open(str(path), "r", encoding="utf-8") as fp:
        return json.load(fp)


def get_candidate_by_id(all_candidate, candidate_id):
    """    - возвращает одного кандидата по его id"""
    for uid in all_candidate:
        if int(uid["id"]) == int(candidate_id):
            return uid


def get_candidates_by_name(all_candidate, candidate_name):
    """— возвращает кандидатов по имени"""
    for candidate in all_candidate:
        if candidate["name"] == candidate_name:
            return candidate


def get_candidates_by_skill(all_candidate, skill_name):
    filtred_candidate = []
    """— возвращает кандидатов по skills"""
    for candidate in all_candidate:
        if skill_name.lower() in candidate["skills"].lower().split(', '):
            filtred_candidate.append(candidate)
    return filtred_candidate


if DEBUG:
    pprint(get_candidate_by_id(load_candidates_from_json(PATH), 2))
    pprint(get_candidates_by_skill(load_candidates_from_json(PATH), "go"))
