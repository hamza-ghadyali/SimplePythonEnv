# %%

mymsg = "after installing the VS Code Jupyter Extension, Run Cell shows up but still doesn't work"
mymsg
# Strangely, I get a message from VS code asking to install ipykernel, which is already installed.
# Previously, ipykernel was only installed likely because it was a dependency of jupyterlab.
# By adding ipykernel to the requirements.txt file and rebuilding container, everything works

# %%

startjupyterlab = "jupyter lab --ip 0.0.0.0 --no-browser --allow-root"