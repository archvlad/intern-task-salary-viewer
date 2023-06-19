<template>
    <div>
        <h3>Текущая зарплата:</h3>
        <h3><b>{{ aboutMe.salary }}₽</b></h3>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            aboutMe: ""
        };
    },
    async mounted() {
        try {
            let response = await axios.get("me");
            this.aboutMe = response.data;
            console.log(response.data)
        } catch (e) {
            console.log(e.response.statusText)
            if (e.response.statusText == 'Unauthorized') {
                this.$router.push('/login')
            }
        }
    },
}
</script>

<style scoped>
p {
    word-wrap: break-word;
}

.nav_links {
    background-color: beige;
    display: flex;
}

a {
    text-decoration: none;
}

div {
    text-align: center;
}
</style>