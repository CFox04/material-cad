import React, { useState } from "react";
import {
    Button,
    TextField,
    Link,
    Grid,
    Typography,
    Container,
} from "@material-ui/core";
import PasswordField from "./PasswordField";
import useStyles from "./style";
import { axiosInstance } from "../../axios";
import { useHistory } from "react-router-dom";

function Register() {
    const history = useHistory();
    const initialFormData = Object.freeze({
        email: "",
        password: "",
        confirmPassword: "",
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
        if (formData.password === formData.confirmPassword) {
            e.preventDefault();
            console.log(formData);

            axiosInstance
                .post(`user/register/`, {
                    email: formData.email,
                    password: formData.password,
                })
                .then((res) => {
                    history.push("/login");
                    console.log(res);
                    console.log(res.data);
                });
        } else {
            console.log("Passwords do not match");
        }
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
                        textFieldProps={{
                            onChange: handleChange,
                        }}
                    />
                    <PasswordField
                        textFieldProps={{
                            name: "confirmPassword",
                            label: "Confirm Password",
                            onChange: handleChange,
                        }}
                    />
                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        color="primary"
                        className={classes.submit}
                        onClick={handleSubmit}
                    >
                        Sign Up
                    </Button>
                    <Grid container>
                        <Grid item>
                            <Link href="/login" variant="body2">
                                Already have an account?
                            </Link>
                        </Grid>
                    </Grid>
                </form>
            </div>
        </Container>
    );
}

export default Register;
