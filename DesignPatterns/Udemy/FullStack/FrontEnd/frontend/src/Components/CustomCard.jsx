import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import { Button, Typography } from '@mui/material'
import { makeStyles } from '@mui/styles'

const useStyles = makeStyles({
    divStyle: {
        width: "100%",
        border:"2px solid red",
        padding:"15px",
    },

    btnStyle: {
        backgroundColor: "yellow",
    }
});

const CustomCard = () => {
    const [btnColor, setBtnColor] = useState("error");
    const classes = useStyles();
  return (
        <div className={classes.divStyle}>
            <Typography variant="h4">This is the title</Typography>
            <Typography variant="body1">Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Nemo suscipit necessitatibus laudantium sint, sit non ab omnis ullam porro temporibus maiores! Consequatur asperiores, facere distinctio quam dignissimos numquam! Quos, adipisci quia ipsa perferendis distinctio, cumque quasi officia doloribus quaerat reiciendis, ad et? Officia consequuntur harum in eos suscipit doloremque sapiente nostrum ut inventore, non eaque excepturi obcaecati vel eius, voluptatum quidem iste quasi accusantium ex autem deleniti eveniet? Impedit voluptate nulla et quae vero voluptatibus at nostrum cum, similique veritatis quo, cumque odio. Obcaecati facere, doloribus dolores aspernatur, totam nisi sequi exercitationem quidem eum a non aut? Esse eos id minima velit rerum quis ea. Accusantium, impedit! Eaque deleniti expedita nobis possimus officiis dignissimos suscipit! Sint laborum voluptates, exercitationem animi fugiat natus perferendis itaque ad distinctio? Perferendis reprehenderit, cumque esse architecto expedita voluptatem asperiores molestias! Praesentium corrupti quasi unde eaque deleniti, at nulla sequi nam molestias ullam alias illo possimus deserunt debitis voluptas odio nobis dolorem inventore cum aspernatur. Nobis expedita ea officiis aliquid at dolores adipisci voluptas, deleniti cupiditate doloribus assumenda vel, molestiae minus alias cum, est consequuntur. Quasi corporis minus rerum quia eos temporibus, sunt possimus modi dignissimos,
            praesentium odio, explicabo id aliquam provident eaque obcaecati perferendis illo.</Typography>
            <Button
                onClick={() => setBtnColor("success")} 
                color={btnColor} 
                variant="contained" 
                size="large"
                className={classes.btnStyle}>
                Turn Green
            </Button>
        </div>
  )
}

export default CustomCard