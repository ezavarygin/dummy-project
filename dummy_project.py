import streamlit as st
import plotly.figure_factory as ff
from dummy_src.distributions import clipped_normal_sample


mean1 = st.slider('Mean value 1', min_value=-10., max_value=10., value=-5., step=0.1)
mean2 = st.slider('Mean value 2', min_value=-10., max_value=10., value=3., step=0.1)

std1 = st.slider('Standard deviation 1', min_value=0., max_value=3., value=1., step=0.1)
std2 = st.slider('Standard deviation 2', min_value=0., max_value=3., value=0.5, step=0.1)

size1 = st.slider('Sample size 1', min_value=1, max_value=1000, value=500, step=1)
size2 = st.slider('Sample size 2', min_value=1, max_value=1000, value=100, step=1)

lower = None
upper = None

data1 = clipped_normal_sample(mean1, std1, size1, lower=lower, upper=upper)
data2 = clipped_normal_sample(mean2, std2, size2, lower=lower, upper=upper)

hist_data = [data1, data2]
group_labels = ['Sample 1', 'Sample 2']

fig = ff.create_distplot(hist_data, group_labels, bin_size=1.)
fig.update_traces(nbinsx=20, autobinx=True, selector={'type': 'histogram'}, marker_line_width=1)

st.plotly_chart(fig, use_container_width=True)
