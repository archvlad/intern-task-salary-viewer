<template>
    <div>
        <h3>Дата следующего повышения:</h3>
        <h3><b>{{ humanDate(aboutMe.next_increase) }}</b></h3>
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
    methods: {
        humanDate(date) {
            return new Date(date).toLocaleString('ru', {
                year: 'numeric',
                month: 'long',
                day: 'numeric'
            });
        }
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

a {
    text-decoration: none;
}

div {
    text-align: center;
    margin: 15px;
}
</style>