
# FBPS Questions (Q1-Q25)
# Scale: 1 = Disagree, 5 = Agree
FBPS_QUESTIONS = [
    {"id": "Q1",  "text": "I am good at keeping track of multiple tasks."},
    {"id": "Q2",  "text": "I feel responsible for the wellbeing of others."},
    {"id": "Q3",  "text": "I often take charge in group situations."},
    {"id": "Q4",  "text": "I tend to be well organized."},
    {"id": "Q5",  "text": "I feel the need to set a good example for others."},
    {"id": "Q6",  "text": "I am comfortable making decisions for others."},
    {"id": "Q7",  "text": "I tend to be serious and goal oriented."},
    {"id": "Q8",  "text": "I feel a strong sense of duty."},
    {"id": "Q9",  "text": "I am good at mediating conflicts."},
    {"id": "Q10", "text": "I tend to be a perfectionist."},
    {"id": "Q11", "text": "I feel that I have to justify my actions to others."},
    {"id": "Q12", "text": "I am good at taking care of others."},
    {"id": "Q13", "text": "I tend to be conservative and conventional."},
    {"id": "Q14", "text": "I feel comfortable in positions of authority."},
    {"id": "Q15", "text": "I tend to plan ahead."},
    {"id": "Q16", "text": "I feel a strong sense of loyalty to my family."},
    {"id": "Q17", "text": "I tend to be reliable and dependable."},
    {"id": "Q18", "text": "I feel the need to achieve and succeed."},
    {"id": "Q19", "text": "I tend to be cautious and careful."},
    {"id": "Q20", "text": "I feel responsible for solving problems."},
    {"id": "Q21", "text": "I tend to be rebellious and unconventional."},
    {"id": "Q22", "text": "I feel comfortable letting others take charge."},
    {"id": "Q23", "text": "I tend to be spontaneous and impulsive."},
    {"id": "Q24", "text": "I feel comfortable depending on others."},
    {"id": "Q25", "text": "I tend to be laid back and relaxed."},
]

# Big Five Questions
# Scale: 1 = Disagree, 5 = Agree
BIG5_QUESTIONS = [
    # Extraversion (EXT1-EXT10)
    {"id": "EXT1",  "text": "I am the life of the party."},
    {"id": "EXT2",  "text": "I don't talk a lot."},
    {"id": "EXT3",  "text": "I feel comfortable around people."},
    {"id": "EXT4",  "text": "I keep in the background."},
    {"id": "EXT5",  "text": "I start conversations."},
    {"id": "EXT6",  "text": "I have little to say."},
    {"id": "EXT7",  "text": "I talk to a lot of different people at parties."},
    {"id": "EXT8",  "text": "I don't like to draw attention to myself."},
    {"id": "EXT9",  "text": "I don't mind being the center of attention."},
    {"id": "EXT10", "text": "I am quiet around strangers."},

    # Emotional Stability (EST1-EST10)
    {"id": "EST1",  "text": "I get stressed out easily."},
    {"id": "EST2",  "text": "I am relaxed most of the time."},
    {"id": "EST3",  "text": "I worry about things."},
    {"id": "EST4",  "text": "I seldom feel blue."},
    {"id": "EST5",  "text": "I am easily disturbed."},
    {"id": "EST6",  "text": "I get upset easily."},
    {"id": "EST7",  "text": "I change my mood a lot."},
    {"id": "EST8",  "text": "I have frequent mood swings."},
    {"id": "EST9",  "text": "I get irritated easily."},
    {"id": "EST10", "text": "I often feel blue."},

    # Agreeableness (AGR1-AGR10)
    {"id": "AGR1",  "text": "I feel little concern for others."},
    {"id": "AGR2",  "text": "I am interested in people."},
    {"id": "AGR3",  "text": "I insult people."},
    {"id": "AGR4",  "text": "I sympathize with others' feelings."},
    {"id": "AGR5",  "text": "I am not interested in other people's problems."},
    {"id": "AGR6",  "text": "I have a soft heart."},
    {"id": "AGR7",  "text": "I am not really interested in others."},
    {"id": "AGR8",  "text": "I take time out for others."},
    {"id": "AGR9",  "text": "I feel others' emotions."},
    {"id": "AGR10", "text": "I make people feel at ease."},

    # Conscientiousness (CSN1-CSN10)
    {"id": "CSN1",  "text": "I am always prepared."},
    {"id": "CSN2",  "text": "I leave my belongings around."},
    {"id": "CSN3",  "text": "I pay attention to details."},
    {"id": "CSN4",  "text": "I make a mess of things."},
    {"id": "CSN5",  "text": "I get chores done right away."},
    {"id": "CSN6",  "text": "I often forget to put things back in their proper place."},
    {"id": "CSN7",  "text": "I like order."},
    {"id": "CSN8",  "text": "I shirk my duties."},
    {"id": "CSN9",  "text": "I follow a schedule."},
    {"id": "CSN10", "text": "I am exacting in my work."},

    # Openness (OPN1-OPN10)
    {"id": "OPN1",  "text": "I have a rich vocabulary."},
    {"id": "OPN2",  "text": "I have difficulty understanding abstract ideas."},
    {"id": "OPN3",  "text": "I have a vivid imagination."},
    {"id": "OPN4",  "text": "I am not interested in abstract ideas."},
    {"id": "OPN5",  "text": "I have excellent ideas."},
    {"id": "OPN6",  "text": "I do not have a good imagination."},
    {"id": "OPN7",  "text": "I am quick to understand things."},
    {"id": "OPN8",  "text": "I use difficult words."},
    {"id": "OPN9",  "text": "I spend time reflecting on things."},
    {"id": "OPN10", "text": "I am full of ideas."},
]

# All questions in order
ALL_QUESTIONS = FBPS_QUESTIONS + BIG5_QUESTIONS

# Country list for dropdown
COUNTRIES = [
    "US", "GB", "CA", "AU", "DE", "FR", "IN", "MY", "PH", "ID",
    "SE", "NZ", "DK", "BR", "NO", "FI", "NL", "BE", "CH", "AT",
    "IE", "IT", "ES", "PT", "PL", "CZ", "HU", "RO", "GR", "SG",
    "PK", "BD", "LK", "CN", "JP", "KR", "TH", "VN", "HK", "TW",
    "AR", "CL", "CO", "PE", "VE", "MX", "ZA", "NG", "KE", "GH",
    "EG", "OTHER"
]