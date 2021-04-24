import React from "react";
import {
    BrowserRouter as Router,
    Route,
    Redirect,
    Switch,
} from "react-router-dom";
import ReactDOM from "react-dom";
import "./index.css";
import CssBaseline from "@material-ui/core/CssBaseline";
import { createMuiTheme, ThemeProvider } from "@material-ui/core";
import blue from "@material-ui/core/colors/blue";
import grey from "@material-ui/core/colors/grey";
import Home from "./components/home/Home";
import Login from "./components/user/Login";
import Logout from "./components/user/Logout";
import Register from "./components/user/Register";
import Footer from "./components/common/Footer";
import Header from "./components/common/Header";
import ErrorBoundary from "./components/common/ErrorBoundary";
import NotFound from "./components/common/NotFound";
import Police from "./components/police/Police";

// Material UI theme
const theme = createMuiTheme({
    palette: {
        type: "dark",
        primary: {
            light: blue[400],
            main: blue[600],
            dark: blue[800],
        },
        background: {
            paper: "#2F2F2F",
            default: "#292929",
        },
        disabled: grey["800"],
    },
    overrides: {
        MuiCssBaseline: {
            "@global": {
                html: {
                    position: "relative",
                    margin: "0 2em",
                },
            },
        },
    },
});

// Check if logged in
// const isLoggedIn = () => localStorage.getItem("access_token") != null;
function isLoggedIn() {
    return (
        (localStorage.getItem("access_token") &&
        localStorage.getItem("refresh_token")) && (localStorage.getItem("access_token") !== "undefined" && localStorage.getItem("refresh_token") !== "undefined"))
}

ReactDOM.render(
    <React.StrictMode>
        <Router forceRefresh={true}>
            <ThemeProvider theme={theme}>
                <CssBaseline />
                {isLoggedIn() && <Header />}
                <ErrorBoundary>
                    <Switch>
                        {/* Re route unauthenticated users to the login page */}
                        <Route exact path="/">
                            {!isLoggedIn() ? (
                                <Redirect to="/login" />
                            ) : (
                                <Home />
                            )}
                        </Route>
                        {/* Re route authenticated users to the home page */}
                        <Route exact path="/login">
                            {isLoggedIn() ? <Redirect to="/" /> : <Login />}
                        </Route>
                        <Route path="/register" component={Register} />
                        <Route path="/logout" component={Logout} />
                        <Route path="/police" component={Police} />
                        <Route component={NotFound} />
                    </Switch>
                </ErrorBoundary>
                <Footer />
            </ThemeProvider>
        </Router>
    </React.StrictMode>,
    document.getElementById("root")
);
