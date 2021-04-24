import React from "react";
import Card from "./Card";
import { Typography, Grid } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import { ReactComponent as PersonIcon } from "../../images/person.svg";
import { ReactComponent as PoliceIcon } from "../../images/police.svg";
import { ReactComponent as EmsIcon } from "../../images/ems.svg";
import { ReactComponent as FireIcon } from "../../images/fire.svg";

const useStyles = makeStyles((theme) => ({
    title: {
        fontSize: 54,
        fontFamily: "SignPainter, Roboto",
        textShadow: "1px 4px #000000",
        padding: "0.5em",
    },
    mainContainer: {
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        height: "80%",
        width: "100%",
        padding: "1em",
    },
}));

function Home() {
    const classes = useStyles();

    return (
        <div className={classes.mainContainer}>
            <Typography className={classes.title} component="h1" variant="h2">
                Sunnyvale Roleplay
            </Typography>
            <Grid container direction="row" justify="center">
                <Card img={PersonIcon} href="/civilian">
                    CIVILIAN
                </Card>
                <Card img={PoliceIcon} href="/police">
                    POLICE
                </Card>
                <Card img={EmsIcon} disabled={true}>
                    EMS
                </Card>
                <Card img={FireIcon} disabled={true}>
                    FIRE
                </Card>
            </Grid>
        </div>
    );
}

export default Home;
