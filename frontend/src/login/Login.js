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
import { axiosInstance } from "../axios";
import { useHistory } from "react-router-dom";

function Login() {
    const history = useHistory();
    const initialFormData = Object.freeze({
        email: "",
        password: "",
    });

    const [formData, updateFormData] = useState(initialFormData);

    const handleChange = (e) => {
        updateFormData({
            ...formData,
            // Trimming any whitespace
            [e.target.name]: e.target.value.trim(),
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(formData);

        axiosInstance
            .post(`token/`, {
                email: formData.email,
                password: formData.password,
            })
            .then((res) => {
                localStorage.setItem("access_token", res.data.access);
                localStorage.setItem("refresh_token", res.data.refresh);
                axiosInstance.defaults.headers["Authorization"] =
                    "JWT" + localStorage.getItem("access_token");
                // Wait for token to set before redirecting
                setTimeout(() => {
                    history.push("/");
                }, 100);
                // console.log(res);
                // console.log(res.data);
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
                    <FormControlLabel
                        control={<Checkbox value="remember" color="primary" />}
                        label="Remember me"
                    />
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
