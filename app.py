import streamlit as st
import pandas as pd
from func import *
from streamlit_extras.mention import mention

def main():

	st.set_page_config(page_title="MovieHub", page_icon="📽️", layout="centered", initial_sidebar_state="expanded")

	st.markdown(""" <style>
	#MainMenu {visibility: hidden;}
	footer {visibility: hidden;}
	</style> """, unsafe_allow_html=True)

	menu = ["Home","Movies","People", "Creators"]
	choice = st.sidebar.radio(" ",menu)

	if choice == "Home":
		st.title("MovieHub📽️")
		st.header("Welcome to MovieHub!!")
		st.text("Having difficulty choosing what to watch? Not Anymore")
		my_expander1 = st.expander("**What is MovieHub?**")
		my_expander1.write("....")
		my_expander2 = st.expander("**How does it work?**")
		my_expander2.write("....")
		my_expander3 = st.expander("**How to use MovieHub?**")
		my_expander3.write("....")

	elif choice == "Movies":
		# if(st.button("Show Movies")):
		with st.expander("List of Movies:"):
			result = view_movies()
			clean_df = pd.DataFrame(result,columns=['Title', 'Release Year', 'Runtime (in minutes)'])
			# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
			st.dataframe(clean_df)

		st.write("**Filters:**")
		ryear = st.number_input("Release Year",step=1)
		rate = st.number_input("Minimum Rating",min_value=0, max_value=10,step=1)
		length = st.selectbox("Length of Movie", ["None", "Short Film", "Feature Film"])
		earn = st.selectbox('Earning', ["None","Profit", "Loss"])

		if(ryear>1950 and rate>0 and length!="None" and earn!="None"):
			result = filterbyrelease_rating_length_earning(ryear,rate,length,earn)
			clean_df = pd.DataFrame(result,columns=['Title', 'Release Year', 'Rating', 'Runtime (in minutes)','Earning'])
			# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
			st.dataframe(clean_df)

		elif(ryear>1950 and rate>0 and length!="None"):
			result = filterbyrelease_rating_length(ryear,rate,length)
			clean_df = pd.DataFrame(result,columns=['Title', 'Release Year', 'Rating', 'Runtime (in minutes)'])
			# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
			st.dataframe(clean_df)
		
		elif(ryear>1950 and rate>0 and earn!="None"):
			result = filterbyrelease_rating_earning(ryear,rate,earn)
			clean_df = pd.DataFrame(result,columns=['Title', 'Release Year', 'Rating','Earning'])
			# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
			st.dataframe(clean_df)
		
		elif(ryear>1950 and length!="None" and earn!="None"):
			result = filterbyrelease_length_earning(ryear,length,earn)
			clean_df = pd.DataFrame(result,columns=['Title', 'Release Year', 'Runtime (in minutes)','Earning'])
			# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
			st.dataframe(clean_df)

		elif(rate>0 and length!="None" and earn!="None"):
			result = filterbyrating_length_earning(rate,length,earn)
			clean_df = pd.DataFrame(result,columns=['Title', 'Release Year', 'Rating', 'Runtime (in minutes)','Earning'])
			# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
			st.dataframe(clean_df)

		elif(ryear>1950 and rate>0):
			result = filterbyrelease_rating(ryear,rate)
			clean_df = pd.DataFrame(result,columns=['Title', 'Release Year', 'Rating', 'Overview'])
			# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
			st.dataframe(clean_df)
		
		elif(ryear>1950 and length!="None"):
			if(length=="Short Film"):
				result = filterbyrelease_length(ryear,"Short")
				clean_df = pd.DataFrame(result,columns=['Title', 'Release Year', 'Runtime (in minutes)', 'Overview'])
				# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
				st.dataframe(clean_df)
			else:
				result = filterbyrelease_length(ryear,"Feature")
				clean_df = pd.DataFrame(result,columns=['Title', 'Release Year', 'Runtime (in minutes)', 'Overview'])
				# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
				st.dataframe(clean_df)
		
		elif(ryear>1950 and earn!="None"):
			if(earn=="Profit"):
				result = filterbyrelease_earning(ryear,"Profit")
				clean_df = pd.DataFrame(result,columns=['Title', 'Release Year','Overview','Earning'])
				# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
				st.dataframe(clean_df)
			else:
				result = filterbyrelease_earning(ryear,"Loss")
				clean_df = pd.DataFrame(result,columns=['Title', 'Release Year','Overview','Earning'])
				# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
				st.dataframe(clean_df)

		elif(rate>0 and length!="None"):
			if(length=="Short Film"):
				result = filterbyrating_length(rate,"Short")
				clean_df = pd.DataFrame(result,columns=['Title', 'Release Year', 'Rating', 'Runtime (in minutes)'])
				# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
				st.dataframe(clean_df)
			else:
				result = filterbyrating_length(rate,"Feature")
				clean_df = pd.DataFrame(result,columns=['Title', 'Release Year', 'Rating', 'Runtime (in minutes)'])
				# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
				st.dataframe(clean_df)

		elif(rate>0 and earn!="None"):
			if(earn=="Profit"):
				result = filterbyrating_earning(rate,"Profit")
				clean_df = pd.DataFrame(result,columns=['Title', 'Release Year', 'Rating','Earning'])
				# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
				st.dataframe(clean_df)
			else:
				result = filterbyrating_earning(rate,"Loss")
				clean_df = pd.DataFrame(result,columns=['Title', 'Release Year', 'Rating','Earning'])
				# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
				st.dataframe(clean_df)
		
		elif(length!="None" and earn!="None"):
			if(length=="Short Film"):
				if(earn=="Profit"):
					result = filterbylength_earning("Short","Profit")
					clean_df = pd.DataFrame(result,columns=['Title', 'Release Year', 'Runtime (in minutes)','Earning'])
					# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
					st.dataframe(clean_df)
				else:
					result = filterbylength_earning("Short","Loss")
					clean_df = pd.DataFrame(result,columns=['Title', 'Release Year', 'Runtime (in minutes)','Earning'])
					# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
					st.dataframe(clean_df)
			else:
				if(earn=="Profit"):
					result = filterbylength_earning("Feature","Profit")
					clean_df = pd.DataFrame(result,columns=['Title', 'Release Year', 'Runtime (in minutes)','Earning'])
					# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
					st.dataframe(clean_df)
				else:
					result = filterbylength_earning("Feature","Loss")
					clean_df = pd.DataFrame(result,columns=['Title', 'Release Year', 'Runtime (in minutes)','Earning'])
					# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
					st.dataframe(clean_df)

		else:
			if(ryear>1950):
				result = filterbyyear(ryear)
				clean_df = pd.DataFrame(result,columns=['Title', 'Overview', 'Runtime (in minutes)'])
				# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
				st.dataframe(clean_df)
			
			elif(rate>0):
				result = filterbyrating(rate)
				clean_df = pd.DataFrame(result,columns=['Title', 'Release Year', 'Rating', 'Overview'])
				# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
				st.dataframe(clean_df)
				
			
			elif(length!="None"):
				if(length=="Short Film"):
					result = filterbyruntime("Short")
					clean_df = pd.DataFrame(result,columns=['Title', 'Release Year', 'Runtime (in minutes)', 'Overview'])
					# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
					st.dataframe(clean_df)
				else:
					result = filterbyruntime("Feature")
					clean_df = pd.DataFrame(result,columns=['Title', 'Release Year', 'Runtime (in minutes)', 'Overview'])
					# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
					st.dataframe(clean_df)
			
			elif(earn!="None"):
				if(earn=="Profit"):
					result = filterbyearning("Profit")
					clean_df = pd.DataFrame(result,columns=['Title', 'Release Year','Overview','Earning'])
					# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
					st.dataframe(clean_df)
				else:
					result = filterbyearning("Loss")
					clean_df = pd.DataFrame(result,columns=['Title', 'Release Year','Overview','Earning'])
					# clean_df['runtime'] = clean_df['runtime'].fillna("Not Available")
					st.dataframe(clean_df)

	elif choice == "People":
		with st.expander("List of People:"):
			result = view_people()
			clean_df = pd.DataFrame(result,columns=['Name', 'Profession', 'Gender', 'Birthyear'])
			clean_df['Profession'] = clean_df['Profession'].fillna("Not Available")
			st.dataframe(clean_df)

		st.write("**Filters:**")
		gender = st.selectbox("Gender",["None", "Male", "Female"])
		profession = st.text_input("Profession")
		age = st.number_input("Age",min_value=0,step=1)

		if(gender!='None' and age>0 and len(profession)>0):
			result = filterbygender_age_prof(gender,age,profession)
			clean_df = pd.DataFrame(result,columns=['Name', 'Profession', 'Gender', 'Age','Birthyear','Deathyear'])
			# clean_df['Profession'] = clean_df['Profession'].fillna("Not Available")
			st.dataframe(clean_df)

		elif(gender!='None' and len(profession)>0):
			result = filterbygender_prof(gender,profession)
			clean_df = pd.DataFrame(result,columns=['Name', 'Profession', 'Gender', 'Birthyear'])
			# clean_df['Profession'] = clean_df['Profession'].fillna("Not Available")
			st.dataframe(clean_df)

		elif(gender!='None' and age>0):
			result = filterbygender_age(gender,age)
			clean_df = pd.DataFrame(result,columns=['Name', 'Profession', 'Age','Birthyear','Deathyear'])
			clean_df['Profession'] = clean_df['Profession'].fillna("Not Available")
			st.dataframe(clean_df)

		elif(len(profession)>0 and age>0):
			result = filterbyage_prof(age,profession)
			clean_df = pd.DataFrame(result,columns=['Name', 'Profession', 'Age','Birthyear','Deathyear'])
			clean_df['Profession'] = clean_df['Profession'].fillna("Not Available")
			st.dataframe(clean_df)

		else:
			if(gender != "None"):
				result = filterbygender(gender)
				clean_df = pd.DataFrame(result,columns=['Name', 'Profession', 'Gender', 'Birthyear'])
				clean_df['Profession'] = clean_df['Profession'].fillna("Not Available")
				st.dataframe(clean_df)

			elif(len(profession)>0):
				result = filterbyprofession(profession)
				clean_df = pd.DataFrame(result,columns=['Name','Profession','Gender','Birthyear'])
				# clean_df['Profession'] = clean_df['Profession'].fillna("Not Available")
				st.dataframe(clean_df)
			
			elif(age>0):
				result = filterbyage(age)
				clean_df = pd.DataFrame(result,columns=['Name','Age','Birthyear','Deathyear'])
				# clean_df['Deathyear'] = clean_df['Deathyear'].fillna("Is Alive")
				st.dataframe(clean_df)

	elif choice == "Creators":
		tab1, tab2, tab3, tab4= st.tabs(["Kartik Jain", "Manas Agarwal", "Neev Swarnakar", "Uttkarsh Singh"])
		with tab1:
			st.header("Kartik Jain")
			# st.image("photos\kartik_jain.jpeg",width=250)
			st.write("I am a fourth-year Computer Science and Social Science Undergraduate at IIIT Delhi. I am an academically goal-driven individual who has strong problem-solving skills. I am open to new experiences and opportunities.")
			st.write("Socials:")
			mention(label="Github",icon="github",  url="https://github.com/Kartik20440")
			mention(label="Linkedin",icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/900px-LinkedIn_logo_initials.png?20140125013055",  url="https://www.linkedin.com/in/kartikxjain/")
			st.write("kartik20440@iiitd.ac.in")

		with tab2:
			st.header("Manas Agarwal")
			# st.image("photos\manas_agarwal.jpg", width=250)
			st.write("I am a 4th Year Undergrad at IIIT Delhi pursuing a Bachelor of Technology majoring in Computer Science.\nI love playing with Data Structures and Algorithms and am highly interested in Problem Solving.\nI am working as a researcher with MIDAS labs and also a Teaching Assistant at IIITD.")
			st.write("Socials:")
			mention(label="Github",icon="github",  url="https://github.com/manas20443")
			mention(label="Linkedin",icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/900px-LinkedIn_logo_initials.png?20140125013055",  url="https://www.linkedin.com/in/manas-agarwal-a63170215/")
			st.write("manas20443@iiitd.ac.in")
		
		with tab3:
			st.header("Neev Swarnakar")
			# st.image("photos\Rishabh_oberoi.jpg", width=200)
			st.write("As a passionate 4th year Computer Science student, I love exploring the fascinating worlds of data structures and algorithms, mathematics, and cognitive science. \nI find it thrilling to dive deep into complex concepts and uncover their practical applications, always striving to learn and grow as a problem-solver.")
			st.write("Socials:")
			mention(label="Github",icon="github",  url="https://github.com/neev13")
			mention(label="Linkedin",icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/900px-LinkedIn_logo_initials.png?20140125013055",  url="https://www.linkedin.com/in/neev-swarnakar-278050201/")
			st.write("neev20390@iiitd.ac.in")

		with tab4:
			st.header("Uttkarsh Singh")
			# st.image("photos\\utkarsh_singh.jpeg", width=250)
			st.write("As a senior at IIIT Delhi, I have a strong interest in data structures and algorithms, and I am passionate about solving real-world problems through programming. I have completed several projects where I have applied my skills in software development.")
			st.write("Socials:")
			mention(label="Github",icon="github",  url="https://github.com/uttkxrrsh")
			mention(label="Linkedin",icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/900px-LinkedIn_logo_initials.png?20140125013055",  url="https://www.linkedin.com/in/uttkarshsingh/")
			st.write("uttkarsh20479@iiitd.ac.in")


if __name__ == '__main__':
	main()
