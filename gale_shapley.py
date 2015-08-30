def is_new_partner_better(female_preference, old_partner, new_male_partner):
    return female_preference.index(new_male_partner) < female_preference.index(old_partner)


def gale_shapley(male_preferences, female_preferences):
    unpaired_males = set(range(1, len(male_preferences) + 1))
    female_pairing = {}
    while len(unpaired_males) > 0:
        new_single_male = unpaired_males.pop()
        for female_candidate in male_preferences[new_single_male - 1]:
            if female_candidate in female_pairing:
                old_male_pair = female_pairing[female_candidate]
                if is_new_partner_better(female_preferences[female_candidate - 1], old_male_pair,
                                         new_single_male):
                    female_pairing[female_candidate] = new_single_male
                    unpaired_males.add(old_male_pair)
                    break
            else:
                female_pairing[female_candidate] = new_single_male
                break

    return set(map(lambda (f, m): (m, f), female_pairing.iteritems()))
