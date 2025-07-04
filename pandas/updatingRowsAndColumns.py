people={
    "first":["Corey","Jane","John"],
    "last":["Schafer","Doe","Doe"],
    "email":["CoreyMSchafer@gmail.com","JaneDoe@gmail.com","JohnDoe@gmail.com"]
}
import pandas as pd
df=pd.DataFrame(people)
print("\n",df)
df.columns=['first_name','last_name','email']
df.columns= df.columns.str.replace(' ','_') # replace space with underscores
print("\n",df)
df.rename(columns={'first_name':'first','last_name':'last'},inplace=True)
print("\n",df)
df.loc[2]=['John','Smith','JohnSmith@email.com']
print("\n",df) #updating values of row
df.loc[2,['last','email']] =['Doe','JohnDoe@gmail.com']
print("\n",df) # changing particular columns 
df.loc[2,'last']='Smith'
print("\n",df) #changing one value
df.at[2,'last']='Doe'
print("\n",df) # at is also used to change a single value
filt=(df['email']=='JohnDoe@gmail.com')
print("\n",df[filt])
filt=df['email']=='JohnDoe@gmail.com'
df.loc[filt,'last']='Smith'
print("\n",df)
print("\n",df['email'].apply(len))#showing the length of all email address
def update_email(email):
    return email.upper()
print("\n",df['email'].apply(update_email))
df['email']=df['email'].apply(lambda x:x.lower())
print("\n",df)
print("\n",df.apply(len))#this is applying len function to each series of the dataframe not all values this  is showing the first have a length of 3 that is three values and with the all the other columns 
print("\n",df.apply(pd.Series.min))
df.apply(lambda x:x.min())