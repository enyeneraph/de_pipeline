cat "/opt/airflow/src/files/new_jobs.csv" >> "/opt/airflow/src/files/jobs.csv"

cd /opt/airflow/src/files \
&& if git status | find "jobs.csv" ; then
  git remote set-url origin https://${GH_NAME}:${GH_TOKEN}@github.com/${GH_NAME}/${REPO}.git && 
  git add "jobs.csv" &&
  echo "Adding file to staging." &&
  git commit -m "Committing changes on $(date +"%Y-%m-%d") to jobs.csv" &&
  echo "Committing..." &&
  git push -u origin main && echo "Pushed..."
fi
