import pandas as pd
import streamlit as st
from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski

# Grab the Lipinski's Values
def lipinski(smile):
	# Convert into Chem object
	mol = Chem.MolFromSmiles(smile)

	MolWt = Descriptors.MolWt(mol)
	MolLogP = Descriptors.MolLogP(mol)
	NumHDonors = Lipinski.NumHDonors(mol)
	NumHAcceptors = Lipinski.NumHAcceptors(mol)

	return NumHDonors, NumHAcceptors, MolWt, MolLogP


st.title("Molecular Descriptors Calculator")
st.header("What is Lipinski's rule?")
st.markdown("> A rule of thumb to evaluate druglikeness or determine if a chemical compound with a certain pharmacological or biological activity has chemical properties and physical properties that would make it a likely orally active drug in humans")

st.header("Components of the rule")
st.markdown(">1. **No more than 5** hydrogen bond donors (the total number of nitrogen–hydrogen and oxygen–hydrogen bonds)\n2. **No more than 10** hydrogen bond acceptors (all nitrogen or oxygen atoms)\n3. A molecular mass **less than 500 daltons**\n4. An octanol-water partition coefficient (log P) that **does not exceed 5**")


# Take User Input Smile
st.header("Input SMILE")
user_smile = st.text_input("Enter text below")

# Calculation
hDonar = (lipinski(user_smile)[0])
hAccep = (lipinski(user_smile)[1])
molWgt = (lipinski(user_smile)[2])
logPVa = (lipinski(user_smile)[3])

st.header("Lipinski's Descriptors Values")

st.write(pd.DataFrame({

	'H Donars': pd.Series(hDonar),
	'H Acceptors': pd.Series(hAccep),
	'Molecular Mass (Dalton)': pd.Series(molWgt),
	'LogP': pd.Series(logPVa)
		}))