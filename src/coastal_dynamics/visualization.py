import warnings

import numpy as np
import pandas as pd
import panel as pn

pn.extension()

warnings.filterwarnings("ignore", category=FutureWarning, module="holoviews.core.data")


class DynamicWavePlot(pn.viewable.Viewer):
    """
    A class for creating a dynamic wave plot with adjustable parameters.

    This class uses Panel widgets to create an interactive visualization
    of a sine wave, where the amplitude 'a' and wavelength 'L' can be adjusted.

    Attributes:
        amplitude_slider (pn.widgets.FloatSlider): Slider to adjust the amplitude.
        wavelength_slider (pn.widgets.FloatSlider): Slider to adjust the wavelength.
        plot (pn.Column): A Panel Column containing the dynamic plot.
    """

    def __init__(
        self,
        amplitude_range: tuple[float, float, float],
        wavelength_range: tuple[float, float, float],
    ):
        """Inits DynamicWavePlot with ranges for amplitude and wavelength sliders."""
        self.amplitude_slider = pn.widgets.FloatSlider(
            name="Amplitude [a]",
            start=amplitude_range[0],
            end=amplitude_range[1],
            step=amplitude_range[2],
            value=amplitude_range[0],
        )
        self.wavelength_slider = pn.widgets.FloatSlider(
            name="Wavelength [L]",
            start=wavelength_range[0],
            end=wavelength_range[1],
            step=wavelength_range[2],
            value=wavelength_range[0],
        )
        self.plot = pn.bind(
            self.generate_wave_plot, a=self.amplitude_slider, L=self.wavelength_slider
        )

    def generate_wave_plot(self, a: float, L: float):
        """Generates a sine wave plot based on the given amplitude and wavelength."""
        x = np.linspace(0, 12, 100)
        eta = a * np.sin(2 * np.pi / L * x)
        df = pd.DataFrame({"x": x, "eta": eta})
        return df.hvplot.line(x="x", y="eta", grid=True, width=900, height=600)

    def __panel__(self) -> pn.Column:
        """Creates a Panel layout with the sliders and the plot."""
        return pn.Column(self.amplitude_slider, self.wavelength_slider, self.plot)
