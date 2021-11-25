# ![](docs/worldmap.png)
# LEGO World Map in Markley’s Projection

### How to build the website

    jupytext worldmap.py --to ipynb
    jupyter nbconvert --execute worldmap.ipynb --to html --output docs/index.html
