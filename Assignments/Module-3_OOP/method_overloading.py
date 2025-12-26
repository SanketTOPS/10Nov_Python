class student:
    #Method Overloading
    def getdata(self,id):
        print("ID:",id)
        
    def getdata(self,name):
        print("Name:",name)

st=student()
st.getdata(12)
st.getdata("Sanket")