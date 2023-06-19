<template>
    <div>
        <NavBar />
        <div class="container">
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
import NavBar from './NavBar.vue'
export default {
    data() {
        return {
            aboutMe: ""
        };
    },
    components: { NavBar }
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

.container {
    margin: 15px;
}
</style>