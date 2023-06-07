from Backend.app import db

class VoterDetails(db.Model):
    __tablename__ = 'VoterDetails'

    Voter_Details_Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    voter_id = db.Column(db.String(10), unique=True, nullable=False)
    voter_name = db.Column(db.String(100), nullable=False)
    voter_father_name = db.Column(db.String(100))
    address = db.Column(db.Text)
    street = db.Column(db.Text)
    ward = db.Column(db.Text)
    phone_number = db.Column(db.BigInteger)
    whatsapp_number = db.Column(db.BigInteger)
    voter_gender = db.Column(db.String(25))
    voter_marital_status = db.Column(db.String(25))
    voter_age = db.Column(db.Integer)
    voter_educational_qualification = db.Column(db.String(25))
    voter_profession = db.Column(db.String(25))
    voter_income_per_month = db.Column(db.Integer)
    voter_income_per_year = db.Column(db.Integer)
    voter_family_income_per_month = db.Column(db.Integer)
    number_of_votes_in_voters_family = db.Column(db.Integer)
    number_of_votes_in_voters_extended_family = db.Column(db.Integer)
    voter_caste = db.Column(db.String(25))
    voter_political_party = db.Column(db.String(100))
    whether_voter_is_politically_neutral = db.Column(db.String(25))
    whether_voter_is_getting_government_benefits = db.Column(db.String(25))
    whether_voters_family_is_getting_government_benefits = db.Column(db.String(25))
    voter_work_location = db.Column(db.Text)
    whether_voter_accepts_money_from_political_party = db.Column(db.String(25))
    whether_voters_family_accepts_money_from_political_party = db.Column(db.String(25))
    number_of_police_cases_on_voter = db.Column(db.Integer)
    number_of_police_cases_on_voters_family_members = db.Column(db.Integer)
    voter_has_own_house = db.Column(db.String(25))
    whether_voter_is_migrated_from_another_place = db.Column(db.String(25))
    voter_opinion_on_present_government = db.Column(db.Text)
    opinion_label_on_present_government = db.Column(db.String(25))
    voter_opinion_on_local_MLA = db.Column(db.Text)
    opinion_label_on_local_MLA = db.Column(db.String(25))
    local_MLA_political_party = db.Column(db.String(100), db.ForeignKey('PoliticalParties.Party_Name'))
    voter_opinion_on_opposition_party_MLA_candidate = db.Column(db.Text)
    opinion_label_on_opposition_party_MLA_candidate = db.Column(db.String(25))
    opposition_party_MLA_candidate_political_party = db.Column(db.String(100), db.ForeignKey('PoliticalParties.Party_Name'))
    voter_opinion_on_local_coporator_or_village_president = db.Column(db.Text)
    opinion_label_on_local_coporator_or_village_president = db.Column(db.String(25))
    local_coporator_political_party = db.Column(db.String(100), db.ForeignKey('PoliticalParties.Party_Name'))
    which_political_party_you_wish_to_vote = db.Column(db.String(100), db.ForeignKey('PoliticalParties.Party_Name'))
    BPL = db.Column(db.String(25))
    reservation_category = db.Column(db.String(25))
    voting_first_time = db.Column(db.String(25))
    constituency_name = db.Column(db.String(100), db.ForeignKey('AssemblyConstituency.Constituency_Name'))
    polling_booth_name = db.Column(db.String(100))
    polling_booth_no = db.Column(db.Integer)
    pincode = db.Column(db.Integer)
    latitude = db.Column(db.Text)
    longitude = db.Column(db.Text)
    is_voter_handicap = db.Column(db.String(25))
    number_of_members_visited_foreign_country_in_voters_family = db.Column(db.Integer)
    number_of_dependents_of_the_voter = db.Column(db.Integer)
    voter_religion = db.Column(db.String(25))
    voter_has_own_car = db.Column(db.String(25))
    voter_has_own_bike = db.Column(db.String(25))
    voter_mother_tongue = db.Column(db.String(25))
    voter_monthly_spending = db.Column(db.Integer)
    voter_family_monthly_spending = db.Column(db.Integer)
    voted_in_last_election = db.Column(db.String(25))

    def __init__(self, voter_id, voter_name, voter_father_name, address, street, ward, phone_number, 
                 whatsapp_number, voter_gender, voter_marital_status, voter_age, voter_educational_qualification, voter_profession, 
                 voter_income_per_month, voter_income_per_year, voter_family_income_per_month, number_of_votes_in_voters_family, 
                 number_of_votes_in_voters_extended_family, voter_caste, voter_political_party, whether_voter_is_politically_neutral,
                 whether_voter_is_getting_government_benefits, whether_voters_family_is_getting_government_benefits, voter_work_location,
                 whether_voter_accepts_money_from_political_party, whether_voters_family_accepts_money_from_political_party, number_of_police_cases_on_voter, 
                 number_of_police_cases_on_voters_family_members, voter_has_own_house, whether_voter_is_migrated_from_another_place, voter_opinion_on_present_government, 
                 opinion_label_on_present_government, voter_opinion_on_local_MLA, opinion_label_on_local_MLA, local_MLA_political_party, voter_opinion_on_opposition_party_MLA_candidate, 
                 opinion_label_on_opposition_party_MLA_candidate, opposition_party_MLA_candidate_political_party, voter_opinion_on_local_coporator_or_village_president, 
                 opinion_label_on_local_coporator_or_village_president, local_coporator_political_party, which_political_party_you_wish_to_vote, BPL, reservation_category, voting_first_time,
                 constituency_name, polling_booth_name, polling_booth_no, pincode, latitude, longitude, is_voter_handicap, number_of_members_visited_foreign_country_in_voters_family, 
                 number_of_dependents_of_the_voter, voter_religion, voter_has_own_car, voter_has_own_bike, voter_mother_tongue, voter_monthly_spending, voter_family_monthly_spending, voted_in_last_election):
        self.voter_id = voter_id
        self.voter_name = voter_name
        self.voter_father_name = voter_father_name
        self.address = address
        self.street = street
        self.ward = ward
        self.phone_number = phone_number
        self.whatsapp_number = whatsapp_number
        self.voter_gender = voter_gender
        self.voter_marital_status = voter_marital_status
        self.voter_age = voter_age
        self.voter_educational_qualification = voter_educational_qualification
        self.voter_profession = voter_profession
        self.voter_income_per_month = voter_income_per_month
        self.voter_income_per_year = voter_income_per_year
        self.voter_family_income_per_month = voter_family_income_per_month
        self.number_of_votes_in_voters_family = number_of_votes_in_voters_family
        self.number_of_votes_in_voters_extended_family = number_of_votes_in_voters_extended_family
        self.voter_caste = voter_caste
        self.voter_political_party = voter_political_party
        self.whether_voter_is_politically_neutral = whether_voter_is_politically_neutral
        self.whether_voter_is_getting_government_benefits = whether_voter_is_getting_government_benefits
        self.whether_voters_family_is_getting_government_benefits = whether_voters_family_is_getting_government_benefits
        self.voter_work_location = voter_work_location
        self.whether_voter_accepts_money_from_political_party = whether_voter_accepts_money_from_political_party
        self.whether_voters_family_accepts_money_from_political_party = whether_voters_family_accepts_money_from_political_party
        self.number_of_police_cases_on_voter = number_of_police_cases_on_voter
        self.number_of_police_cases_on_voters_family_members = number_of_police_cases_on_voters_family_members
        self.voter_has_own_house = voter_has_own_house
        self.whether_voter_is_migrated_from_another_place = whether_voter_is_migrated_from_another_place
        self.voter_opinion_on_present_government = voter_opinion_on_present_government
        self.opinion_label_on_present_government = opinion_label_on_present_government
        self.voter_opinion_on_local_MLA = voter_opinion_on_local_MLA
        self.opinion_label_on_local_MLA = opinion_label_on_local_MLA
        self.local_MLA_political_party = local_MLA_political_party
        self.voter_opinion_on_opposition_party_MLA_candidate = voter_opinion_on_opposition_party_MLA_candidate
        self.opinion_label_on_opposition_party_MLA_candidate = opinion_label_on_opposition_party_MLA_candidate
        self.opposition_party_MLA_candidate_political_party = opposition_party_MLA_candidate_political_party
        self.voter_opinion_on_local_coporator_or_village_president = voter_opinion_on_local_coporator_or_village_president
        self.opinion_label_on_local_coporator_or_village_president = opinion_label_on_local_coporator_or_village_president
        self.local_coporator_political_party = local_coporator_political_party
        self.which_political_party_you_wish_to_vote = which_political_party_you_wish_to_vote
        self.BPL = BPL
        self.reservation_category = reservation_category
        self.voting_first_time = voting_first_time
        self.constituency_name = constituency_name
        self.polling_booth_name = polling_booth_name
        self.polling_booth_no = polling_booth_no
        self.pincode = pincode
        self.latitude = latitude
        self.longitude = longitude
        self.is_voter_handicap = is_voter_handicap
        self.number_of_members_visited_foreign_country_in_voters_family = number_of_members_visited_foreign_country_in_voters_family
        self.number_of_dependents_of_the_voter = number_of_dependents_of_the_voter
        self.voter_religion = voter_religion
        self.voter_has_own_car = voter_has_own_car
        self.voter_has_own_bike = voter_has_own_bike
        self.voter_mother_tongue = voter_mother_tongue
        self.voter_monthly_spending = voter_monthly_spending
        self.voter_family_monthly_spending = voter_family_monthly_spending
        self.voted_in_last_election = voted_in_last_election

