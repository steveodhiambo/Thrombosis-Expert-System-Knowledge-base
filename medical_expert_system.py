from pyknow import *

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

def preprocess():
	global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map
	diseases = open("diseases.txt")
	diseases_t = diseases.read()
	diseases_list = diseases_t.split("\n")
	diseases.close()
	for disease in diseases_list:
		disease_s_file = open("Disease symptoms/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		s_list = disease_s_data.split("\n")
		diseases_symptoms.append(s_list)
		symptom_map[str(s_list)] = disease
		disease_s_file.close()
		disease_s_file = open("Disease descriptions/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_desc_map[disease] = disease_s_data
		disease_s_file.close()
		disease_s_file = open("Disease treatments/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_treatment_map[disease] = disease_s_data
		disease_s_file.close()
	

def identify_disease(*arguments):
	symptom_list = []
	for symptom in arguments:
		symptom_list.append(symptom)
	# Handle key error
	return symptom_map[str(symptom_list)]

def get_details(disease):
	return d_desc_map[disease]

def get_treatments(disease):
	return d_treatment_map[disease]

def if_not_matched(disease):
		print("")
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		print("")
		print("The most probable Thrombosis you have is %s\n" %(id_disease))
		print("Find a short description of the disease given below :\n")
		print(disease_details+"\n")
		print("The common medications and procedures suggested by other real doctors are: \n")
		print(treatments+"\n")

# @my_decorator is just a way of saying just_some_function = my_decorator(just_some_function)
#def identify_disease(headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever,sunken_eyes):
class Greetings(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		print("")
		print("Hi! we are PonaHaraka, we are here to help you make your health better.")
		print("For that you'll have to answer a few YES/NO questions about your conditions \n")
		print("Do you feel any of the following symptoms:")
		print("")
		yield Fact(action="find_disease")


	@Rule(Fact(action='find_disease'), NOT(Fact(fever=W())),salience = 13)
	def symptom_0(self):
		self.declare(Fact(fever=input("Fever: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(light_headedness=W())),salience = 12)
	def symptom_1(self):
		self.declare(Fact(light_headedness=input("Light_headedness: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(headache=W())),salience = 11)
	def symptom_2(self):
		self.declare(Fact(headache=input("Headache: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(chest_pain=W())),salience = 10)
	def symptom_3(self):
		self.declare(Fact(chest_pain=input("Chest Pain: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(leg_pain=W())),salience = 9)
	def symptom_4(self):
		self.declare(Fact(leg_pain=input("Leg pains: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(swollen_leg=W())),salience = 8)
	def symptom_5(self):
		self.declare(Fact(swollen_leg=input("Swelling in the leg(s): ")))
	 
	@Rule(Fact(action='find_disease'), NOT(Fact(swollen_arm=W())),salience = 7)
	def symptom_6(self):
		self.declare(Fact(swollen_arm=input("Swelling in the arm(s): ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(swollen_neck_face=W())),salience = 6)
	def symptom_7(self):
		self.declare(Fact(swollen_neck_face=input("Swelling in the neck & face: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(abdominal_swelling=W())),salience = 5)
	def symptom_8(self):
		self.declare(Fact(abdominal_swelling=input("Abdominal swelling: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(coughing_blood=W())),salience = 4)
	def symptom_9(self):
		self.declare(Fact(coughing_blood=input("Coughing Blood: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(fatigue=W())),salience = 3)
	def symptom_10(self):
		self.declare(Fact(fatigue=input("Fatigue: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(skin_discoloration=W())),salience = 2)
	def symptom_11(self):
		self.declare(Fact(skin_discoloration=input("Skin Discoloration: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(breathing_fast=W())),salience = 1)
	def symptom_12(self):
		self.declare(Fact(breathing_fast=input("Breathing Fast: ")))

	@Rule(Fact(action='find_disease'),Fact(fever="no"),Fact(light_headedness="yes"),Fact(headache="no"),Fact(chest_pain="yes"),Fact(leg_pain="yes"),Fact(swollen_leg="yes"),Fact(swollen_arm="no"),Fact(swollen_neck_face="no"),Fact(abdominal_swelling="no"),Fact(coughing_blood="yes"),Fact(fatigue="yes"),Fact(skin_discoloration="no"),Fact(breathing_fast="yes"))
	def disease_0(self):
		self.declare(Fact(disease="PulmonaryEmbolism"))

	@Rule(Fact(action='find_disease'),Fact(fever="no"),Fact(light_headedness="no"),Fact(headache="no"),Fact(chest_pain="no"),Fact(leg_pain="yes"),Fact(swollen_leg="yes"),Fact(swollen_arm="no"),Fact(swollen_neck_face="no"),Fact(abdominal_swelling="no"),Fact(coughing_blood="no"),Fact(fatigue="no"),Fact(skin_discoloration="yes"),Fact(breathing_fast="no"))
	def disease_1(self):
		self.declare(Fact(disease="DeepVein"))

	@Rule(Fact(action='find_disease'),Fact(fever="yes"),Fact(light_headedness="no"),Fact(headache="no"),Fact(chest_pain="no"),Fact(leg_pain="no"),Fact(swollen_leg="yes"),Fact(swollen_arm="no"),Fact(swollen_neck_face="no"),Fact(abdominal_swelling="yes"),Fact(coughing_blood="no"),Fact(fatigue="no"),Fact(skin_discoloration="no"),Fact(breathing_fast="no"))
	def disease_2(self):
		self.declare(Fact(disease="FemoralVein"))

	@Rule(Fact(action='find_disease'),Fact(fever="no"),Fact(light_headedness="no"),Fact(headache="no"),Fact(chest_pain="no"),Fact(leg_pain="no"),Fact(swollen_leg="no"),Fact(swollen_arm="yes"),Fact(swollen_neck_face="no"),Fact(abdominal_swelling="no"),Fact(coughing_blood="no"),Fact(fatigue="no"),Fact(skin_discoloration="yes"),Fact(breathing_fast="no"))
	def disease_3(self):
		self.declare(Fact(disease="Paget-SchroetterSyndrome"))

	@Rule(Fact(action='find_disease'),Fact(fever="no"),Fact(light_headedness="yes"),Fact(headache="no"),Fact(chest_pain="yes"),Fact(leg_pain="no"),Fact(swollen_leg="no"),Fact(swollen_arm="no"),Fact(swollen_neck_face="no"),Fact(abdominal_swelling="no"),Fact(coughing_blood="no"),Fact(fatigue="no"),Fact(skin_discoloration="no"),Fact(breathing_fast="yes"))
	def disease_4(self):
		self.declare(Fact(disease="MyocardialInfarction(Heart Attack)"))

	@Rule(Fact(action='find_disease'),Fact(fever="no"),Fact(light_headedness="yes"),Fact(headache="yes"),Fact(chest_pain="no"),Fact(leg_pain="no"),Fact(swollen_leg="no"),Fact(swollen_arm="yes"),Fact(swollen_neck_face="yes"),Fact(abdominal_swelling="no"),Fact(coughing_blood="no"),Fact(fatigue="no"),Fact(skin_discoloration="no"),Fact(breathing_fast="yes"))
	def disease_5(self):
		self.declare(Fact(disease="SuperiorVenaCava"))

	@Rule(Fact(action='find_disease'),Fact(fever="yes"),Fact(light_headedness="yes"),Fact(headache="yes"),Fact(chest_pain="no"),Fact(leg_pain="no"),Fact(swollen_leg="no"),Fact(swollen_arm="yes"),Fact(swollen_neck_face="no"),Fact(abdominal_swelling="no"),Fact(coughing_blood="no"),Fact(fatigue="no"),Fact(skin_discoloration="yes"),Fact(breathing_fast="no"))
	def disease_6(self):
		self.declare(Fact(disease="JugularVein"))

	@Rule(Fact(action='find_disease'),Fact(fever="no"),Fact(light_headedness="no"),Fact(headache="yes"),Fact(chest_pain="no"),Fact(leg_pain="no"),Fact(swollen_leg="no"),Fact(swollen_arm="yes"),Fact(swollen_neck_face="no"),Fact(abdominal_swelling="yes"),Fact(coughing_blood="no"),Fact(fatigue="yes"),Fact(skin_discoloration="no"),Fact(breathing_fast="no"))
	def disease_7(self):
		self.declare(Fact(disease="Stroke"))

	@Rule(Fact(action='find_disease'),Fact(fever="yes"),Fact(light_headedness="yes"),Fact(headache="yes"),Fact(chest_pain="no"),Fact(leg_pain="no"),Fact(swollen_leg="no"),Fact(swollen_arm="no"),Fact(swollen_neck_face="yes"),Fact(abdominal_swelling="no"),Fact(coughing_blood="yes"),Fact(fatigue="yes"),Fact(skin_discoloration="no"),Fact(breathing_fast="no"))
	def disease_8(self):
		self.declare(Fact(disease="CerebralVenousSinus"))

	@Rule(Fact(action='find_disease'),Fact(fever="yes"),Fact(light_headedness="no"),Fact(headache="yes"),Fact(chest_pain="no"),Fact(leg_pain="no"),Fact(swollen_leg="no"),Fact(swollen_arm="no"),Fact(swollen_neck_face="no"),Fact(abdominal_swelling="yes"),Fact(coughing_blood="yes"),Fact(fatigue="no"),Fact(skin_discoloration="no"),Fact(breathing_fast="no"))
	def disease_9(self):
		self.declare(Fact(disease="PortalVein"))

	@Rule(Fact(action='find_disease'),Fact(fever="no"),Fact(light_headedness="no"),Fact(headache="no"),Fact(chest_pain="no"),Fact(leg_pain="no"),Fact(swollen_leg="no"),Fact(swollen_arm="no"),Fact(swollen_neck_face="no"),Fact(abdominal_swelling="no"),Fact(coughing_blood="no"),Fact(fatigue="yes"),Fact(skin_discoloration="no"),Fact(breathing_fast="no"))
	def disease_10(self):
		self.declare(Fact(disease="RenalVein"))

	@Rule(Fact(action='find_disease'),Fact(fever="no"),Fact(light_headedness="no"),Fact(headache="no"),Fact(chest_pain="no"),Fact(leg_pain="no"),Fact(swollen_leg="no"),Fact(swollen_arm="no"),Fact(swollen_neck_face="yes"),Fact(abdominal_swelling="no"),Fact(coughing_blood="no"),Fact(fatigue="no"),Fact(skin_discoloration="yes"),Fact(breathing_fast="no"))
	def disease_11(self):
		self.declare(Fact(disease="CavernousSinus"))

	@Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998)
	def disease(self, disease):
		print("")
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		print("")
		print("The most probable Thrombosis that you have is %s\n" %(id_disease))
		print("Find below a short description of the disease :\n")
		print(disease_details+"\n")
		print("The common medications and procedures suggested by other real doctors are: \n")
		print(treatments+"\n")

	@Rule(Fact(action='find_disease'),
		  Fact(fever=MATCH.fever),
		  Fact(light_headedness=MATCH.light_headedness),
		  Fact(headache=MATCH.headache),
		  Fact(chest_pain=MATCH.chest_pain),
		  Fact(leg_pain=MATCH.leg_pain),
		  Fact(swollen_leg=MATCH.swollen_leg),
		  Fact(swollen_arm=MATCH.swollen_arm),
		  Fact(swollen_neck_face=MATCH.swollen_neck_face),
		  Fact(abdominal_swelling=MATCH.abdominal_swelling),
		  Fact(coughing_blood=MATCH.coughing_blood),
		  Fact(fatigue=MATCH.fatigue),
		  Fact(skin_discoloration=MATCH.skin_discoloration),
		  Fact(breathing_fast=MATCH.breathing_fast),NOT(Fact(disease=MATCH.disease)),salience = -999)

	def not_matched(self,fever, light_headedness, headache, chest_pain, leg_pain, swollen_leg, swollen_arm, swollen_neck_face, abdominal_swelling ,coughing_blood ,fatigue ,skin_discoloration ,breathing_fast):
		print("\nDid not find any disease that matches your exact symptoms")
		lis = [fever, light_headedness, headache, chest_pain, leg_pain, swollen_leg, swollen_arm, swollen_neck_face, abdominal_swelling ,coughing_blood ,fatigue ,skin_discoloration ,breathing_fast]
		max_count = 0
		max_disease = ""
		for key,val in symptom_map.items():
			count = 0
			temp_list = eval(key)
			for j in range(0,len(lis)):
				if(temp_list[j] == lis[j] and lis[j] == "yes"):
					count = count + 1
			if count > max_count:
				max_count = count
				max_disease = val
		if_not_matched(max_disease)


if __name__ == "__main__":
	preprocess()
	engine = Greetings()
	while(1):
		engine.reset()  # Prepare the engine for the execution.
		engine.run()  # Run it!
		print("Would you like to diagnose some other symptoms?")
		if input() == "no":
			exit()
		#print(engine.facts)