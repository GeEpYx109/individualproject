import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib.ticker import MaxNLocator


st.set_page_config(layout = "wide")
st.title("Потенциал заряженных тел")

def fine_grid(ax, nx = 20, ny = 16):
    ax.xaxis.set_major_locator(MaxNLocator(nbins = nx))
    ax.yaxis.set_major_locator(MaxNLocator(nbins = ny))
    ax.minorticks_on()
    ax.grid(which = "major", alpha = 0.6)
    ax.grid(which = "minor", alpha = 0.2, linestyle = ":")

def show_point():
    q = st.sidebar.slider("Заряд q", 0.5, 5.0, 1.0, key="point_q")

    r = np.logspace(-3, 1, 600)# больше значений около нуля, чтобы было видно, что при r стремящимся к 0 значение потенциала бесконечность
    u = q / r
    st.latex(r"u(r) = \frac{q}{r}")
    fig, ax = plt.subplots(figsize = (12, 6))
    ax.plot(r, u, color="tab:red", label="Точечный заряд")
    ax.set_xlabel("Расстояние от заряда r")
    ax.set_ylabel("Потенциал u(r)")
    ax.set_title("Потенциал точечного заряда")
    fine_grid(ax)
    ax.legend()
    ax.set_xlim(left = 0)
    ax.set_ylim(0, 10 * q)
    st.pyplot(fig)


def show_ball():
    r0 = st.sidebar.slider("Радиус шара r₀", 0.5, 3.0, 1.0, key = "ball_r0")
    rho0 = st.sidebar.slider("Плотность заряда ρ₀", 0.5, 3.0, 1.0, key = "ball_rho0")

    r_max = 10 * r0
    r_inside = np.linspace(0, r0, 200)
    r_outside = np.linspace(r0, r_max, 400)
    u_inside = 2 * np.pi * rho0 * (r0**2 - r_inside**2 / 3)
    u_outside = 4 * np.pi * rho0 * r0**3 / (3 * r_outside)

    Q = 4 / 3 * np.pi * rho0 * r0**3   # полный заряд шара
    st.latex(r"u_{in}(r) = 2\pi\rho_0\left(r_0^2 - \frac{r^2}{3}\right)")
    st.latex(r"u_{out}(r) = \frac{4\pi\rho_0 r_0^3}{3r}")
    st.write(f"Полный заряд шара Q = {Q:.2f}")

    fig, ax = plt.subplots(figsize = (12, 6))
    ax.plot(r_inside, u_inside, color = "tab:blue", label = "Внутри шара")
    ax.plot(r_outside, u_outside, color = "tab:red", label = "Снаружи шара")
    ax.axvline(r0, color = "gray", linestyle = "--", label = "Граница шара")
    ax.set_ylabel("Потенциал u(r)")
    ax.set_xlabel("Расстояние от центра r")
    ax.set_title("Потенциал равномерно заряженного шара")
    fine_grid(ax)
    ax.legend()
    ax.set_xlim(left = 0)
    ax.set_ylim(bottom = 0)
    st.pyplot(fig)
def show_sphere():
    r0 = st.sidebar.slider("Радиус сферы r₀", 0.5, 3.0, 1.0, key = "sphere_r0")
    sigma0 = st.sidebar.slider("Поверхностная плотность σ₀", 0.1, 3.0, 1.0, key = "sphere_sigma0")

    r_max = 10 * r0
    r_inside = np.linspace(0, r0, 200)
    r_outside = np.linspace(r0, r_max, 400)
    u_inside = np.full_like(r_inside, 4 * np.pi * sigma0 * r0)
    u_outside = 4 * np.pi * sigma0 * r0**2 / r_outside

    Q = 4 * np.pi * r0**2 * sigma0
    st.latex(r"u_{in}(r) = 4\pi\sigma_0 r_0")
    st.latex(r"u_{out}(r) = \frac{4\pi\sigma_0 r_0^2}{r}")
    st.write(f"Полный заряд сферы Q = {Q:.2f}")

    fig, ax = plt.subplots(figsize = (12, 6))
    ax.plot(r_inside, u_inside, color = "tab:blue", label = "Внутри сферы")
    ax.plot(r_outside, u_outside, color = "tab:red", label = "Снаружи сферы")
    ax.axvline(r0, color = "gray", linestyle = "--", label = "Сфера r = r₀")
    ax.set_xlabel("Расстояние от центра r")
    ax.set_ylabel("Потенциал u(r)")
    ax.set_title("Потенциал равномерно заряженной сферы")
    fine_grid(ax)
    ax.legend()
    ax.set_xlim(left = 0)
    ax.set_ylim(bottom = 0)
    st.pyplot(fig)


shape = st.sidebar.selectbox("Тело", ["Заряженная точка", "Заряженный шар", "Заряженная сфера"])

if shape == "Заряженная точка":
    show_point()
elif shape == "Заряженный шар":
    show_ball()
elif shape == "Заряженная сфера":
    show_sphere()