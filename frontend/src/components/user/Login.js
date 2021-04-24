import React, { useState } from "react";
import {
    Button,
    TextField,
    FormControlLabel,
    Checkbox,
    Link,
    Grid,
    Typography,
    Container,
} from "@material-ui/core";
import PasswordField from "./PasswordField";
import useStyles from "./style";
import { axiosInstance } from "../../axios";
import { useHistory } from "react-router-dom";

function Login() {
    // Need history to redirect user to / once logged in
    const history = useHistory();
    const initialFormData = Object.freeze({
        email: "",
        password: "",
    });

    const [state, setState] = useState({
        formData: initialFormData,
        message: false,
    });

    const handleChange = (e) => {
        setState({
            formData: {
                ...state.formData,
                // Trimming any whitespace
                [e.target.name]: e.target.value.trim(),
            },
        });
    };

    const stringIsEmpty = (string) => {
        return string.length === 0 || !string.trim();
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        // Validate form
        if (
            stringIsEmpty(state.formData.email) ||
            stringIsEmpty(state.formData.password)
        ) {
            setState({ message: "Please enter both your email and password." });
            return;
        }

        axiosInstance
            // Request JWT tokens given the email and password
            .post(`token/`, {
                email: state.formData.email,
                password: state.formData.password,
            })
            .then((res) => {
                // Set the tokens in local storage
                localStorage.setItem("access_token", res.data.access);
                localStorage.setItem("refresh_token", res.data.refresh);
                // Set authorization header of the axios instance
                axiosInstance.defaults.headers["Authorization"] =
                    "JWT" + localStorage.getItem("access_token");
                history.push("/");
            })
            .catch((err) => {
                if (err.response) {
                    if (err.response.status === 401) {
                        setState({
                            message: "Incorrect email and/or password",
                        });
                    }
                }
            });
    };

    const classes = useStyles();

    return (
        <Container className={classes.container} component="main" maxWidth="s">
            <Typography className={classes.title} component="h1" variant="h2">
                Sunnyvale Roleplay
            </Typography>
            <div className={classes.paper}>
                <Typography
                    className={classes.subtitle}
                    component="h2"
                    variant="h6"
                >
                    MDT/CAD SYSTEM
                </Typography>
                <form className={classes.form} noValidate>
                    {state.message && (
                        <span className={classes.error}>{state.message}</span>
                    )}
                    <TextField
                        variant="filled"
                        margin="normal"
                        required
                        fullWidth
                        id="email"
                        label="Email Address"
                        name="email"
                        autoComplete="email"
                        autoFocus
                        onChange={handleChange}
                    />
                    <PasswordField
                        textFieldProps={{ onChange: handleChange }}
                    />
                    {/* <FormControlLabel
                        control={<Checkbox value="remember" color="primary" />}
                        label="Remember me"
                    /> */}
                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        color="primary"
                        className={classes.submit}
                        onClick={handleSubmit}
                    >
                        Sign In
                    </Button>
                    <Grid container>
                        <Grid item xs>
                            <Link href="#" variant="body2">
                                Forgot password?
                            </Link>
                        </Grid>
                        <Grid item>
                            <Link href="/register" variant="body2">
                                {"Don't have an account? Sign Up"}
                            </Link>
                        </Grid>
                    </Grid>
                </form>
            </div>
        </Container>
    );
}

export default Login;
