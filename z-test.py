import numpy as np
import streamlit as st

st.title("Two samples z-test calculator")

p1 = st.number_input("Percentage in the first group (%):", min_value=float(0), max_value=float(100),
                     value=float(0), step=float(0.01))
p2 = st.number_input("Percentage in the second group(%):", min_value=float(0), max_value=float(100),
                     value=float(0), step=float(0.01))
n1 = st.number_input("Size of the first group:", min_value=float(2), max_value=float(10000000000), value=float(100),
                     step=float(1))
n2 = st.number_input("Size of the second group:", min_value=float(2), max_value=float(10000000000), value=float(100),
                     step=float(1))
p_pooled = (p1/100*n1 + p2/100*n2)/(n1+n2)

z = round((p1/100 - p2/100) / np.sqrt((p_pooled*(1-p_pooled))*(1/n1 + 1/n2)), 2)


ci = st.radio("Choose significance level: ", ('95%', '99%'))
sig_99 = 'The test is significant at the 99% level'
not_sig_99 = 'The test is not significant at the 99% level'
sig_95 = 'The test is significant at the 95% level'
not_sig_95 = 'The test is not significant at the 95% level'

def test_sig(z):
    if ci == '95%' and z >= 1.96:
        return sig_95
    elif ci == '95%' and z < 1.96:
        return not_sig_95
    elif ci == '99%' and z >= 2.576:
        return sig_99
    else:
        return not_sig_99

message = test_sig(z)

st.write('z = ' + str(z) + ' ' + message)


