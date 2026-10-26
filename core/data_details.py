# coding: utf8

import matplotlib
# Used to convert binary data (like a PNG image) into plain text, so the chart, for example, can be embedded directly inside an HTML page.
import base64
# Used to give you in-memory file objects (io.BytesIO), so charts can be saved to memory instead of writing image files to disk.
import io
import datetime
# Not an import, but it matters: switches matplotlib to the "Agg" backend, which draws images without opening a window. Needed on servers.
matplotlib.use('Agg')
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from matplotlib.figure import Figure
from matplotlib.ticker import MaxNLocator



# Color for each genre. Put this at the top of data_details.py (outside the class).
# Any genre not listed here falls back to gray, so nothing breaks.
GENRE_COLORS = {
    "Action": "#e63946",       # red
    "Horror": "#f77f00",       # orange
    "Drama": "#7b2cbf",        # purple
    "Comedy": "#ffd166",       # yellow
    "Sci-Fi": "#00b4d8",       # cyan
    "Romance": "#ff70a6",      # pink
    "Thriller": "#6c757d",     # slate
    "Animation": "#06d6a0",    # mint
    "Adventure": "#2a9d8f",    # teal
    "Crime": "#264653",        # dark blue-green
    "Fantasy": "#9d4edd",      # violet
    "Mystery": "#3a86ff",      # blue
    "Documentary": "#8d6e63",  # brown
}
DEFAULT_COLOR = "#adb5bd"      # gray, used for unlisted genres or movies with no genre


class NewDataDetails:
	def __init__(self):
		pass

	@staticmethod
	def bar_plot():
		# Data set
		height = [3, 12, 5, 18, 45]
		bars = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi']
		y_pos = np.arange(len(bars))
		
		# Initialize layout (Figure instead of plt.subplots, so no GUI is involved)
		fig = Figure(figsize=(9, 6))
		ax = fig.subplots()

		# Basic bar plot
		ax.bar(y_pos, height, color=(0.2, 0.4, 0.6, 0.6))
		ax.set_title('Total num of genres')
		ax.set_xlabel('Most watched movie genres')
		ax.set_ylabel('Num of Genres')
		ax.set_xticks(y_pos)
		ax.set_xticklabels(bars)
		ax.tick_params(axis='x', colors='red', direction='out', length=13, width=3)
		
		# Custom Axis title
		#ax.clabel('title of the xlabel', fontweight='bold', color = 'orange', fontsize='17', horizontalalignment='center')

		# Save to memory and encode as text so it can go inside HTML
		buffer = io.BytesIO()
		fig.savefig(buffer, format="png", bbox_inches="tight")
		return base64.b64encode(buffer.getvalue()).decode("ascii")

	@staticmethod
	def time_chart():
		# Create dataframe
		dataframe = pd.DataFrame({
			'date_when_watched': [
				datetime.datetime(2021, 11, i + 1)
				for i in range(7)
			],
			'movies_watched': [5, 6, 8, 2, 3, 7, 4]
		})

		# Create figure and axes
		fig = Figure(figsize=(9, 6))
		ax = fig.subplots()

		# Plot the time series
		ax.plot(
			dataframe['date_when_watched'],
			dataframe['movies_watched'],
			marker='o'
		)

		# Configure chart
		ax.set_title('Amount of Movies Watched in Given Week')
		ax.set_xlabel('Week')
		ax.set_ylabel('Movies Watched')
		ax.tick_params(axis='x', labelrotation=30)

		fig.tight_layout()

		# Save to memory and encode as text so it can go inside HTML
		buffer = io.BytesIO()
		fig.savefig(buffer, format="png", bbox_inches="tight")
		return base64.b64encode(buffer.getvalue()).decode("ascii")

	# Scatterplot for Matplotlib
	@staticmethod
	def scatter_plot(movies):
		# Build one row per movie: (year, rating, title, directors, genre).
		# Movies with no rating, or with a release date that doesn't start
		# with a 4-digit year, are skipped so they can't break the chart.
		rows = [
			(
				int(m.release_date[:4]),
				m.rating,
				m.title,
				", ".join(m.directors),
				m.genres[0] if m.genres else "Other",   # first genre only, "Other" if none
			)
			for m in movies
			if m.rating and m.release_date[:4].isdigit()
		]

		# Nothing to plot yet, so let the template show a friendly message instead
		if not rows:
			return None

		# Group the rows by genre: {"Action": [row, row, ...], "Drama": [...]}
		by_genre = {}
		for row in rows:
			by_genre.setdefault(row[4], []).append(row)

		# Figure instead of plt.subplots, so no GUI is involved
		fig = Figure(figsize=(9, 6))
		ax = fig.subplots()

		# One scatter call per genre, so each genre gets its own color and legend entry
		for genre, genre_rows in sorted(by_genre.items()):
			# Only the year and rating are needed here. Titles and directors
			# were for Plotly's hover text, which a static image can't show.
			years, ratings, titles, directors, _ = zip(*genre_rows)

			ax.scatter(
				years,                                        # horizontal axis: release year
				ratings,                                      # vertical axis: the user's rating
				s=80,                                         # dot size (matplotlib uses area, not diameter)
				alpha=0.8,                                    # slight transparency for overlapping dots
				color=GENRE_COLORS.get(genre, DEFAULT_COLOR), # genre color, or gray
				edgecolors="black",                           # thin outline on each dot
				linewidths=1,
				label=genre,                                  # the name shown in the legend
			)

			# Write "Title - (Year)" above each dot in this genre
			for x, y, title in zip(years, ratings, titles):
				ax.annotate(
					f"{title} - ({x})",            # the label text, e.g. "The Matrix - (1999)"
					(x, y),                        # the point being labeled
					xytext=(0, 8),                 # move the text 8 points straight up from the dot
					textcoords="offset points",    # offset is measured in points, not data units
					ha="center",                   # center the text horizontally over the dot
					fontsize=7,
				)

		# Axis labels and a fixed 0-10 scale with a little room above 10
		ax.set_xlabel("Release year")
		ax.set_ylabel("My rating")
		ax.set_ylim(0, 11.5)

		# Whole years only on the x-axis (no "1999.5")
		ax.xaxis.set_major_locator(MaxNLocator(integer=True))

		# Light grid, drawn behind the dots
		ax.grid(True, alpha=0.3)
		ax.set_axisbelow(True)

		# Legend placed outside the plot area, on the right
		ax.legend(title="Genre", loc="center left", bbox_to_anchor=(1.02, 0.5))

		# Save to memory and encode as text so it can go inside HTML
		buffer = io.BytesIO()
		fig.savefig(buffer, format="png", bbox_inches="tight")   # "tight" keeps the outside legend in the image
		return base64.b64encode(buffer.getvalue()).decode("ascii")
		

	@staticmethod
	def scatter_plot_plotly(movies):
		# Build one row per movie: (year, rating, title, directors, genre).
		# Movies with no rating, or with a release date that doesn't start
		# with a 4-digit year, are skipped so they can't break the chart.
		rows = [
			(
				int(m.release_date[:4]),
				m.rating,
				m.title,
				", ".join(m.directors),
				m.genres[0] if m.genres else "Other",   # first genre only, "Other" if none
			)
			for m in movies
			if m.rating and m.release_date[:4].isdigit()
		]

		# Nothing to plot yet, so let the template show a friendly message instead
		if not rows:
			return None

		# Sort the rows into groups, one list of rows per genre:
		# {"Action": [row, row, ...], "Drama": [row, ...]}
		by_genre = {}
		for row in rows:
			by_genre.setdefault(row[4], []).append(row)

		fig = go.Figure()

		# Add one trace (one colored group of dots) for each genre.
		# sorted() keeps the legend in alphabetical order.
		for genre, genre_rows in sorted(by_genre.items()):
			# Split this genre's rows into separate lists, one per column
			years, ratings, titles, directors, _ = zip(*genre_rows)

			fig.add_trace(
				go.Scatter(
					x=years,                  # horizontal axis: release year
					y=ratings,                # vertical axis: the user's rating
					mode="markers",           # dots only, no connecting lines
					name=genre,               # the label shown in the legend
					marker=dict(
						size=12,
						opacity=0.8,
						color=GENRE_COLORS.get(genre, DEFAULT_COLOR),   # genre color, or gray
						line=dict(width=1, color="black"),              # thin outline on each dot
					),

					# Extra data for the hover text (not drawn on the chart):
					# customdata[0] = title, [1] = directors, [2] = genre
					customdata=[(t, d, genre) for t, d in zip(titles, directors)],

					# The text shown when hovering over a dot
					hovertemplate=(
						"<b>%{customdata[0]}</b><br>"
						"Genre: %{customdata[2]}<br>"
						"Directed by %{customdata[1]}<br>"
						"Released: %{x}<br>"
						"Rating: %{y}/10"
						"<extra></extra>"     # hides the default side box showing the trace name
					),
				)
			)

		fig.update_layout(
			template="plotly_white",      # clean white background
			height=500,                   # no fixed width, so the chart fills its container
			xaxis_title="Release year",
			yaxis_title="My rating",
			yaxis=dict(range=[0, 10.5]),  # fixed 0-10 scale, with a little room above 10
			legend_title_text="Genre",
		)

		# Convert the chart to an HTML snippet that can be used in a template
		return pio.to_html(
			fig,
			full_html=False,
			include_plotlyjs="cdn",
			config={"responsive": True, "displaylogo": False},
		)
