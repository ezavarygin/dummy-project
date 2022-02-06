import numpy as np
import streamlit as st

@st.cache(ttl=3600)
def clipped_normal_sample(mean, std, size, lower=None, upper=None):

    rng = np.random.default_rng()
    randn = mean + std * rng.standard_normal(size)

    if lower is None and upper is None:
        return randn

    return randn.clip(min=lower, max=upper)
