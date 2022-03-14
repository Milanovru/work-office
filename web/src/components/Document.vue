<template>
    <div class="html-form">
        <table>
            <tr>
                <td></td>
                <td></td>
                <td>
                    <p v-html="header"></p>
                    <!-- <p>Заместителю начальника отдела – начальнику 2 отделения 13 отдела УИТО Спецсвязи ФСО России<br ><br />полковнику Горжанову А.В.</p> -->
                </td>
            </tr>
        </table>
        <table>
            <tr>
                <td>
                    <p>Рапорт</p>
                </td>
            </tr>
        </table>
        <p>Прошу предоставить мне 1 день отдыха {{date.day+1}} {{date.month}} {{date.year}} года за счет суммированного времени привлечения к исполнению обязанностей военной службы сверх установленной продолжительности еженедельного служебного времени без выезда из Московского гарнизона.
        </p>
        <table>
            <tr>
                <td>
                    <p><input v-model="position" type="text" name="position" id="position" placeholder="Должность"> 2 отделения 13 отдела<br />УИТО Спецсвязи ФСО России<br /><input v-model="rank" type="text" name="rank" id="rank" placeholder="Звание"><br />« {{date.day}} » {{date.month}} {{date.year}} г.</p>
                </td>
                <td>
                    <input v-model="name" type="text" name="name" id="name" placeholder="И.О. Фамилия">
                </td>
            </tr>
        </table>
        <table>
            <tr>
                <td>
                    <p>Согласен</p>
                    <p>«      » {{date.month}} {{date.year}} г.</p>
                </td>
                <td></td>
                <td>
                    <p>Заместителю руководителя <br />Службы – начальнику <br />УИТО Спецсвязи ФСО России<br /></p>
                    <p>генерал-лейтенанту Ермольчику В.Д.</p>
                </td>
            </tr>
        </table>
        <table>
            <tr>
                <td>
                    <p>Ходатайствую по существу рапорта {{rank}}а {{name}}</p>
                </td>
            </tr>
        </table>
        <table>
            <tr>
                <td>
                    <p v-html="footer[0]"></p><p>«      » {{date.month}} {{date.year}} г.</p>
                </td>
                <td>
                    <p v-html="footer[1]"></p>
                </td>
            </tr>
        </table>
    </div>
</template>

<script>
import { useMainStore } from "../stores/mainStore";
import { mapState } from 'pinia'

export default {
    props: {
        header: String,
        footer: Object,
        date: Object
    },
    data() {
        return {
            position: null,
            name: null,
            rank: null,
        }
    },
    methods: {

    },
    computed: {
        
    }
}
</script>

<style lang='less'>

.html-form {
    width: 850px;

    table:nth-child(2) {
        width: 100%;
      td { 
          display: block;
          margin-left: 45%;          
      }
    }

    table:nth-child(4),
    table:nth-child(7) {
        width: 100%;

        td:last-child {
            text-align: right;
        }
    }

    table:nth-child(1),
    table:nth-child(5) {
        tr {
            text-align: center;
            td:nth-child(1) {
                display: block;
                margin-left: 20px;
            }
            td:nth-child(3) {
                display: block;
                margin-left: 280px;
            }
        }
    }

    table:nth-child(6) {
        width: 100%;
        td { 
            display: block;
            margin-left: 15%;
        }
    }

    p:nth-child(3) {
        text-indent: 20px;
        text-align: justify;

    }

}

#rank,
#name,
#position {
    width: 120px;
}

</style>
