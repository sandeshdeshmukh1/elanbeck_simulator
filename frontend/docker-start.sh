#!/bin/sh

# Check if /install/node_modules directory exists and sync
if [ -d /install/node_modules ] ; then
  echo "copying..."
  rsync --owner --group --usermap="*:${APP_UID}" --groupmap="*:${APP_GID}" -Wrlpt -h -H --no-compress --inplace /install/node_modules /app/
fi

# Start the node server based on the environment
if [ "$REACT_APP_ENVIRONMENT" = "production" ]; then
  echo "Starting production node js server..."
  npx serve -s build -p ${FRONTEND_PORT_INTERNAL}
else
  echo "Starting development node js server..."
  npm start
fi
