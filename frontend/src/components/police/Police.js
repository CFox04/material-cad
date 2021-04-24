import React from "react";
import { Box, Grid, Typography, Button, makeStyles } from "@material-ui/core";
import { ReactComponent as PoliceIcon } from "../../images/police.svg";
import ToggleButton from "./ToggleButton";
import BasicTable from "./BasicTable";
import { axiosInstance } from "../../axios";

const useStyles = makeStyles((theme) => ({
    title: {
        // "font-size": 74,
        // "font-family": "SignPainter, Roboto",
        // "text-shadow": "1px 4px #000000",
        fontWeight: 100,
    },
    image: {
        display: "inline",
        width: "3em",
        height: "3em",
        marginRight: "0.5em",
    },
    box: {
        width: "100%",
    },
    headingContainer: {
        // width: "50%",
    },
    buttonContainer: {
        padding: "1em 0",
        "& button": {
            margin: "0.3em",
        },
    },
    panicButton: {
        // borderColor: theme.palette.warning.main,
        backgroundColor: theme.palette.error.main,
        "&:hover": {
            backgroundColor: theme.palette.error.dark,
        },
    },
}));

// const columns = [
//     { field: "id", headerName: "ID", width: 70 },
//     { field: "firstName", headerName: "First name", width: 130 },
//     { field: "lastName", headerName: "Last name", width: 130 },
//     {
//         field: "age",
//         headerName: "Age",
//         type: "number",
//         width: 90,
//     },
//     {
//         field: "fullName",
//         headerName: "Full name",
//         description: "This column has a value getter and is not sortable.",
//         sortable: false,
//         width: 160,
//         valueGetter: (params) =>
//             `${params.getValue("firstName") || ""} ${
//                 params.getValue("lastName") || ""
//             }`,
//     },
// ];

// const rows = [
//     { id: 1, lastName: "Snow", firstName: "Jon", age: 35 },
//     { id: 2, lastName: "Lannister", firstName: "Cersei", age: 42 },
//     { id: 3, lastName: "Lannister", firstName: "Jaime", age: 45 },
//     { id: 4, lastName: "Stark", firstName: "Arya", age: 16 },
//     { id: 5, lastName: "Targaryen", firstName: "Daenerys", age: null },
//     { id: 6, lastName: "Melisandre", firstName: null, age: 150 },
//     { id: 7, lastName: "Clifford", firstName: "Ferrara", age: 44 },
//     { id: 8, lastName: "Frances", firstName: "Rossini", age: 36 },
//     { id: 9, lastName: "Roxie", firstName: "Harvey", age: 65 },
// ];

function Police() {
    const classes = useStyles();
    axiosInstance
        // Request JWT tokens given the email and password
        .get(`characters/`)
        .then((res) => {
            console.log(res);
        })
        .catch((err) => {
            console.log(err);
        });

    return (
        <Grid>
            {/* Heading container */}
            <Box
                className={classes.headingContainer}
                display="flex"
                flexDirection="column"
                justifyContent="flex-start"
            >
                <Box
                    display="flex"
                    flexDirection="row"
                    // justifyContent="center"
                    alignItems="center"
                >
                    <PoliceIcon fill="white" className={classes.image} />
                    <Typography
                        className={classes.title}
                        component="h3"
                        variant="h5"
                    >
                        BLAINE COUNTY SHERIFF'S OFFICE
                    </Typography>
                </Box>
                {/* Buttons container */}
                <Box className={classes.buttonContainer}>
                    <ToggleButton
                        color="warning"
                        onClick={() => console.log("test")}
                    >
                        BUSY
                    </ToggleButton>
                    <ToggleButton
                        color="success"
                        onClick={() => console.log("test")}
                    >
                        AVAILABLE
                    </ToggleButton>
                    <ToggleButton
                        color="danger"
                        onClick={() => console.log("test")}
                    >
                        UNAVAILABLE
                    </ToggleButton>
                    <ToggleButton
                        color="primary"
                        onClick={() => console.log("test")}
                    >
                        ENROUTE
                    </ToggleButton>
                    <ToggleButton
                        color="primary"
                        onClick={() => console.log("test")}
                    >
                        ON SCENE
                    </ToggleButton>
                    <Button color="primary" variant="contained">
                        NOTEPAD
                    </Button>
                    <Button className={classes.panicButton} variant="contained">
                        PANIC
                    </Button>
                </Box>
            </Box>
            <BasicTable title="Current Calls" />
            {/* <EnhancedTable /> */}
        </Grid>
    );
}

export default Police;
