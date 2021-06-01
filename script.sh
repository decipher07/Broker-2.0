eval "$(conda shell.bash hook)"
conda activate
python3 Driver\ Code.py
git add .
now="$(date)"
git commit -m "$now update"
git push origin main
