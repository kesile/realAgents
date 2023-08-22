data = {
    "name": {
        "male": ["John", "Michael", "David", "James", "Robert", "Allen", "William", "Richard", "Joseph", "Charles", "Thomas",
                 "Daniel", "Matthew", "Anthony", "Donald", "Paul", "Mark", "George", "Steven", "Andrew", "Edward",
                 "Brian", "Kevin", "Ronald", "Timothy", "Jason", "Jeffrey", "Scott", "Eric", "Stephen", "Kenneth",
                 "Gary", "Frank", "Patrick", "Gregory", "Joshua", "Bruce", "Johnson", "Jerry", "Dennis", "Walter", "Henry", "Carl",
                 "Arthur", "Ryan", "Roger", "Juan", "Jack", "Albert", "Jonathan", "Justin", "Terry", "Gerald"],
        "female": ["Jane", "Mary", "Jennifer", "Lisa", "Patricia", "Linda", "Barbara", "Elizabeth", "Susan", "Jessica",
                   "Sarah", "Karen", "Nancy", "Margaret", "Betty", "Dorothy", "Helen", "Sandra", "Donna", "Emily",
                   "Carol", "Ruth", "Sharon", "Michelle", "Laura", "Kimberly", "Deborah", "Susan", "Pamela", "Deborah",
                   "Stephanie", "Rebecca", "Cynthia", "Carolyn", "Virginia", "Katherine", "Janet", "Diane", "Alice",
                   "Shirley", "Judith", "Frances", "Joyce", "Christine", "Catherine", "Ann", "Gloria", "Martha",
                   "Julie", "Emma", "Grace"]
    },
    "education" : {
        "No Diploma" : 0.2,
        "Diploma" : 0.4,
        "Bachelors" : 0.2,
        "Masters" : 0.15,
        "PhD" : 0.05
    },
    "weight" : {
        "Underweight" : 0.1,
        "Average weight" : 0.5,
        "Overweight" : 0.3,
        "Obese" : 0.1
    },
    "votes" : {
        "yes" : 0.5,
        "no" : 0.5
    },
    "gender" : {
        "male" : 0.48,
        "female" : 0.48,
        "non-binary" : 0.02,
        "trans-male" : 0.01,
        "trans-female" : 0.01,
    },
    "race" : {
        "White": 60,
        "Black or African American": 15,
        "Asian": 10,
        "Hispanic or Latino": 12,
        "Native American": 2,
        "Other": 1
    },
    "relation" : {
        "Single": 0.30,
        "Married": 0.45,
        "Divorced": 0.13,
        "Widowed": 0.06,
        "Separated": 0.03,
        "Cohabiting": 0.03
    },
    "religion" : {
        "Christian": 0.65,
        "Jewish": 0.02,
        "Muslim": 0.05, 
        "Hindu": 0.01,
        "Buddhist": 0.02,
        "Atheist": 0.10,
        "Agnostic": 0.05,
        "Other": 0.10
    },
    "sexuality": {
        "Heterosexual": 0.90,
        "Homosexual": 0.03,
        "Bisexual": 0.04,
        "Other": 0.03
    },
    "disability": {
        "Yes": 0.15,
        "No": 0.85  
    },
    "location": {
        "Urban": 0.30,
        "Suburban": 0.30,
        "Rural": 0.20,
        "Small town": 0.20   
    },    
    "political": {
        "Democrat": 0.35,
        "Republican": 0.30,
        "Independent": 0.30,
        "Other": 0.05
    },
    "immigration": {
        "US citizen": 0.80,
        "Permanent resident": 0.10,
        "Temporary visa": 0.05,
        "Undocumented": 0.05
    },
    "employment": {
        "Employed": 0.60,
        "Unemployed": 0.05,
        "Retired": 0.15, 
        "Student": 0.10,
        "Disabled": 0.05,
        "Homemaker": 0.05
    },
    "income": {
        "Under $20,000": 0.15,
        "$20,000 - $40,000": 0.20,
        "$40,000 - $60,000": 0.18,
        "$60,000 - $80,000": 0.14,
        "$80,000 - $100,000": 0.12,
        "$100,000 - $150,000": 0.10,
        "Over $150,000": 0.11   
    },
    "age" : {
        "mean" : 35,
        "sd" : 20
    },
    "occupation" : {
        "teacher" : 0.01,
        "chef" : 0.01,
        "engineer" : 0.03,
        "doctor" : 0.02,
        "software developer" : 0.03,
        "nurse" : 0.02,
        "scientist" : 0.02,
        "artist" : 0.02,
        "writer" : 0.02,
        "police officer" : 0.02,
        "firefighter" : 0.01,
        "paramedic" : 0.01,
        "architect" : 0.02,
        "graphic designer" : 0.02,
        "lawyer" : 0.02,
        "accountant" : 0.02,
        "economist" : 0.01,
        "entrepreneur" : 0.02,
        "psychologist" : 0.02,
        "dentist" : 0.01,
        "veterinarian" : 0.01,
        "electrician" : 0.02,
        "plumber" : 0.02,
        "mechanic" : 0.02,
        "carpenter" : 0.02,
        "construction worker" : 0.02,
        "fashion designer" : 0.01,
        "hair stylist" : 0.01,
        "fitness trainer" : 0.01,
        "pilot" : 0.01,
        "flight attendant" : 0.01,
        "chef" : 0.01,
        "waiter/waitress" : 0.02,
        "bartender" : 0.01,
        "hotel manager" : 0.01,
        "tour guide" : 0.01,
        "taxi driver" : 0.01,
        "bus driver" : 0.01,
        "delivery driver" : 0.02,
        "news anchor" : 0.01,
        "journalist" : 0.02,
        "photographer" : 0.02,
        "filmmaker" : 0.01,
        "actor/actress" : 0.01,
        "musician" : 0.02,
        "singer" : 0.01,
        "dancer" : 0.01,
        "athlete" : 0.02,
        "coach" : 0.01,
        "physical therapist" : 0.01,
        "nutritionist" : 0.01,
        "doctor" : 0.02,
        "nurse" : 0.02,
        "pharmacist" : 0.01,
        "paramedic" : 0.01,
        "therapist" : 0.02,
        "social worker" : 0.02,
        "teacher" : 0.01,
        "professor" : 0.02,
        "researcher" : 0.02,
        "scientist" : 0.02,
        "biologist" : 0.01,
        "chemist" : 0.01,
        "physicist" : 0.01,
        "mathematician" : 0.01,
        "historian" : 0.01,
        "archaeologist" : 0.01,
        "psychologist" : 0.02,
        "counselor" : 0.01,
        "therapist" : 0.02,
        "social worker" : 0.02,
        "veterinarian" : 0.01,
        "zookeeper" : 0.01,
        "pet groomer" : 0.01,
        "farmer" : 0.02,
        "gardener" : 0.01,
        "landscaper" : 0.01,
    }
}