import React from "react";
import { BrowserRouter as Router, Route, Redirect } from "react-router-dom";
import ReactDOM from "react-dom";
import "./index.css";
import Login from "./login/Login";
import Register from "./login/Register";
import CssBaseline from "@material-ui/core/CssBaseline";
import { createMuiTheme, ThemeProvider } from "@material-ui/core";
import blue from "@material-ui/core/colors/blue";
import Footer from "./common/Footer";

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
    },
});

// Check if logged in
const loggedIn = localStorage.getItem("access_token") != null;

ReactDOM.render(
    <React.StrictMode>
        <Router>
            <ThemeProvider theme={theme}>
                <CssBaseline />
                <Route exact path="/">
                    {!loggedIn ? <Redirect to="/login" /> : <Redirect to="/" />}
                </Route>
                <Route path="/login" component={Login} />
                <Route path="/register" component={Register} />
                <Footer />
            </ThemeProvider>
        </Router>
    </React.StrictMode>,
    document.getElementById("root")
);
