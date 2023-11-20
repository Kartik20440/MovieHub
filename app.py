# from asyncio.windows_events import NULL
# from unicodedata import name
# import streamlit as st
# import pandas as pd 
# from db_funcs import * 
# import streamlit.components.v1 as stc
# from datetime import date

# import plotly.express as px 

# def main():
# 	menu = ["Home","Register as Buyer","Register as Seller","Sell Product","Update Your Product","View Products","Buy Product","Delete Product","Employee Access","About"]
# 	choice = st.sidebar.selectbox("Menu",menu)

# 	elif choice == "View Products":
# 		st.subheader("Products")
# 		with st.expander("View Data"):
# 			result = view_all_data()
# 			clean_df = pd.DataFrame(result,columns=['product_name', 'product_type', 'price', 'quantity'])
# 			st.dataframe(clean_df)
		
# 		filterbycategory =  st.text_input("Select Category")
# 		filterbyprice =  st.number_input("Select Maximum Price", step=1)
# 		filterbystate =  st.text_input("Select State")

# 		if(len(filterbycategory)!=0) and (filterbyprice > 0) and (len(filterbystate)!=0):
# 			result2 = filter_3category(filterbycategory, filterbyprice, filterbystate)
# 			clean_df = pd.DataFrame(result2,columns=['product_name', 'product_type', 'price', 'quantity','state'])
# 			st.dataframe(clean_df)

# 		elif(len(filterbycategory)!=0) and (filterbyprice > 0):
# 			result2 = filter_4category(filterbycategory, filterbyprice)
# 			clean_df = pd.DataFrame(result2,columns=['product_name', 'product_type', 'price', 'quantity'])
# 			st.dataframe(clean_df)

# 		elif(len(filterbycategory)!=0) and (len(filterbystate) != 0):
# 			result2 = filter_5category(filterbycategory, filterbystate)
# 			clean_df = pd.DataFrame(result2,columns=['product_name', 'product_type', 'price', 'quantity','state'])
# 			st.dataframe(clean_df)

# 		elif(filterbyprice > 0) and (len(filterbystate) != 0):
# 			result2 = filter_6category(filterbyprice, filterbystate)
# 			clean_df = pd.DataFrame(result2,columns=['product_name', 'product_type', 'price', 'quantity','state'])
# 			st.dataframe(clean_df)
		
# 		else:
# 			if(len(filterbycategory)!=0):
# 				result2 = filter_category(filterbycategory)
# 				clean_df = pd.DataFrame(result2,columns=['product_name', 'product_type', 'price', 'quantity'])
# 				st.dataframe(clean_df)
		
# 			elif(filterbyprice > 0):
# 				result2 = filter_price(filterbyprice)
# 				clean_df = pd.DataFrame(result2,columns=['product_name', 'product_type', 'price', 'quantity'])
# 				st.dataframe(clean_df)
			
# 			elif(len(filterbystate)!=0):
# 				result2 = filter_state(filterbystate)
# 				clean_df = pd.DataFrame(result2,columns=['product_name', 'product_type', 'price', 'quantity','state'])
# 				st.dataframe(clean_df)        

# 	elif choice == "Update Your Product":
# 		sid = st.number_input("Enter your Seller ID:",step=1)
# 		if(sid > 0):
# 			with st.expander("Your Products:"):
# 				result = view_seller_specific_data(sid)
# 				clean_df = pd.DataFrame(result,columns=['product_name', 'product_type', 'price', 'quantity','seller_id'])
# 				st.dataframe(clean_df)
# 			list_of_updates = ['None','Product Name','Price','Quantity']
# 			selected_update = st.selectbox("Choose attribute you want to update",list_of_updates)
# 			if(selected_update == 'Product Name'):
# 				oldname = st.text_input("Enter old name:")
# 				pnameup = st.text_input("Enter new name:")
# 				if(len(oldname) > 0 and len(pnameup)>0):
# 					if st.button("Update Product"):
# 						edit_pname(oldname,pnameup,sid)
# 						st.success("Updated Product Name To {}".format(pnameup))
# 						with st.expander("View Updated Data"):
# 							result = view_seller_specific_data(sid)
# 							clean_df = pd.DataFrame(result,columns=['product_name', 'product_type', 'price', 'quantity','seller_id'])
# 							st.dataframe(clean_df)

# 			if(selected_update == 'Price'):
# 				prodname = st.text_input("Enter Product name:")
# 				nprice = st.number_input("Enter new Price:",step=1)
# 				if(len(prodname) > 0 and nprice>0):
# 					if st.button("Update Product"):
# 						edit_pprice(prodname,nprice,sid)
# 						st.success("Updated Product Price To {}".format(nprice))
# 						with st.expander("View Updated Data"):
# 							result = view_seller_specific_data(sid)
# 							clean_df = pd.DataFrame(result,columns=['product_name', 'product_type', 'price', 'quantity','seller_id'])
# 							st.dataframe(clean_df)

# 			if(selected_update == 'Quantity'):
# 				produname = st.text_input("Enter Product name:")
# 				nqty = st.number_input("Enter new Quantity:",step=1)
# 				if(len(produname) > 0 and nqty>0):
# 					if st.button("Update Product"):
# 						edit_pqty(produname,nqty,sid)
# 						st.success("Updated Product Quantity To {}".format(nqty))
# 						with st.expander("View Updated Data"):
# 							result = view_seller_specific_data(sid)
# 							clean_df = pd.DataFrame(result,columns=['product_name', 'product_type', 'price', 'quantity','seller_id'])
# 							st.dataframe(clean_df)

# 	elif choice == "Delete Product":
# 		st.subheader("Delete your Product")
# 		with st.expander("View Data"):
# 			result = view_se_data()
# 			clean_df = pd.DataFrame(result,columns=['product_name', 'product_type', 'price', 'quantity','seller_id'])
# 			st.dataframe(clean_df)

# 		pname =  st.text_input("Enter Product Name:")
# 		psid =  st.number_input("Enter your Seller ID:",step=1)

# 		if st.button("Delete"):
# 			delete_data(pname, psid)
# 			st.warning("Deleted: '{}'".format(pname))

# 		with st.expander("Updated Data"):
# 			result = view_se_data()
# 			clean_df = pd.DataFrame(result,columns=['product_name', 'product_type', 'price', 'quantity', 'seller_id'])
# 			st.dataframe(clean_df)

# 	elif choice == "Buy Product":
# 		st.subheader("Buy Product")
# 		with st.expander("View Data"):
# 			result = view_buy_data()
# 			clean_df = pd.DataFrame(result,columns=['product_id','product_name', 'product_type', 'price', 'quantity','seller_id'])
# 			st.dataframe(clean_df)
		
# 		pid = st.number_input("Enter Product ID",step=1)
# 		sid = st.number_input("Enter Seller ID",step=1)
# 		bname = st.text_input("Buyer Name")
# 		bphno = st.text_input("Buyer Phone No")
# 		datepu = st.date_input("Purchase Date")
# 		payment_method = ['None','UPI','Credit Card','Debit Card']
# 		paymode = st.selectbox("Choose Payment Method-",payment_method)
# 		pamount = st.number_input("Payment Amount",step=1)
# 		if st.button("Place Order"):
# 			payid = place_order(pid, sid, bphno, paymode, pamount,datepu)
# 			st.warning("Your order has been placed with Payment ID: '{}'".format(payid))

# 	elif choice == "Employee Access":
# 		list_of_views = ['None','Transactions','Purchases made by Buyers','Sellers Rating','Sellers Data','Buyers Data']
# 		selected_view = st.selectbox("Choose view:",list_of_views)
# 		if(selected_view == "Transactions"):
# 			with st.expander("View Data"):
# 				result = view_all_transactions()
# 				clean_df = pd.DataFrame(result,columns=['transaction id', 'amount', 'date', 'mode'])
# 				st.dataframe(clean_df)
# 		elif(selected_view == "Purchases made by Buyers"):
# 			with st.expander("View Data"):
# 				result = view_all_purbybuyers()
# 				clean_df = pd.DataFrame(result,columns=['buyer_id', 'product_id', 'amount'])
# 				st.dataframe(clean_df)
# 		elif(selected_view == "Sellers Rating"):
# 			with st.expander("View Data"):
# 				result = view_all_sellers_rating()
# 				clean_df = pd.DataFrame(result,columns=['id', 'name','rating'])
# 				st.dataframe(clean_df)
# 		elif(selected_view == "Sellers Data"):
# 			with st.expander("View Data"):
# 				result = view_all_sellers()
# 				clean_df = pd.DataFrame(result,columns=['id', 'name', 'phone_no','rating'])
# 				st.dataframe(clean_df)
# 		elif(selected_view == "Buyers Data"):
# 			with st.expander("View Data"):
# 				result = view_buyer_data()
# 				clean_df = pd.DataFrame(result,columns=['name','phone_no','email','state','postal_zip','budget'])
# 				st.dataframe(clean_df)
	
# 	elif choice == "About":
# 		st.subheader("Made By-")
# 		st.info("Kartik Jain")
# 		st.info("Jay Saraf")
# 		st.info("Teja Bhavani Shankar Parachoori")
# 		st.info("Vansh Gupta")

# if __name__ == '__main__':
# 	main()


import streamlit as st
from func import *
from streamlit_extras.mention import mention
from streamlit_extras.let_it_rain import rain
from streamlit_extras.no_default_selectbox import selectbox
import time

def main():

	st.set_page_config(page_title="MovieHub", page_icon="📽️", layout="centered", initial_sidebar_state="expanded")

	st.markdown(""" <style>
	#MainMenu {visibility: hidden;}
	footer {visibility: hidden;}
	</style> """, unsafe_allow_html=True)

	# st.sidebar.title("MovieHub📽️")
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

	elif choice == "Creators":
		tab1, tab2, tab3, tab4= st.tabs(["Kartik Jain", "Manas Agarwal", "Neev Swarnakar", "Uttkarsh Singh"])
		with tab1:
			st.header("Kartik Jain")
			# st.image("photos\kartik_jain.jpeg",width=250)
			st.write("I am a third-year Computer Science and Social Science Undergraduate at IIIT Delhi. I am an academically goal-driven individual who has strong problem-solving skills. I am open to new experiences and opportunities.")
			st.write("Socials:")
			mention(label="Github",icon="github",  url="https://github.com/Kartik20440")
			mention(label="Linkedin",icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/900px-LinkedIn_logo_initials.png?20140125013055",  url="https://www.linkedin.com/in/kartikxjain/")
			st.write("kartik20440@iiitd.ac.in")

		with tab2:
			st.header("Manas Agarwal")
			# st.image("photos\manas_agarwal.jpg", width=250)
			st.write("I am a 3rd Year Undergrad at IIIT Delhi pursuing a Bachelor of Technology majoring in Computer Science.\nI love playing with Data Structures and Algorithms and am highly interested in Problem Solving.\nI am working as a researcher with MIDAS labs and also a Teaching Assistant at IIITD.")
			st.write("Socials:")
			mention(label="Github",icon="github",  url="https://github.com/manas20443")
			mention(label="Linkedin",icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/900px-LinkedIn_logo_initials.png?20140125013055",  url="https://www.linkedin.com/in/manas-agarwal-a63170215/")
			st.write("manas20443@iiitd.ac.in")
		
		with tab3:
			st.header("Neev Swarnakar")
			# st.image("photos\Rishabh_oberoi.jpg", width=200)
			st.write("As a passionate 3rd year Computer Science student, I love exploring the fascinating worlds of data structures and algorithms, mathematics, and cognitive science. \nI find it thrilling to dive deep into complex concepts and uncover their practical applications, always striving to learn and grow as a problem-solver.")
			st.write("Socials:")
			mention(label="Github",icon="github",  url="https://github.com/neev13")
			mention(label="Linkedin",icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/900px-LinkedIn_logo_initials.png?20140125013055",  url="https://www.linkedin.com/in/neev-swarnakar-278050201/")
			st.write("neev20390@iiitd.ac.in")

		with tab4:
			st.header("Uttkarsh Singh")
			# st.image("photos\\utkarsh_singh.jpeg", width=250)
			st.write("As a junior at IIIT Delhi, I have a strong interest in data structures and algorithms, and I am passionate about solving real-world problems through programming. I have completed several projects where I have applied my skills in software development.")
			st.write("Socials:")
			mention(label="Github",icon="github",  url="https://github.com/uttkxrrsh")
			mention(label="Linkedin",icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/900px-LinkedIn_logo_initials.png?20140125013055",  url="https://www.linkedin.com/in/uttkarshsingh/")
			st.write("uttkarsh20479@iiitd.ac.in")


if __name__ == '__main__':
	main()
