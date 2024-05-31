import { Route, Navigate } from "react-router-dom";
import { useState, useEffect } from "react";
import DataService from "./Service";
import {RouterPath} from "../../assets/dictionary/RouterPath"

export const PrivateRoute = ({ children }) => {
  const [isAuth, setIsAuth] = useState(true);
  const [isLoaded, setisLoaded] = useState(false);

  useEffect(() => {
    DataService.getAuth()
      .then((response) => {
        setisLoaded(true);
        setIsAuth(true);
      })
      .catch((error) => {
        setisLoaded(true);
        setIsAuth(false);
      });
  }, []);

  if (isLoaded) {
    if (isAuth) {
      return children;
    } else {
      return <Navigate to={RouterPath.LOGIN} />;
    }
  } else {
    return null;
  }
};
