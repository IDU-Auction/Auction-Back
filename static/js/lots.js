$(document).ready(function() {
    var districtOptions = {
        tashkent: ["Bektemir", "Chilanzar", "Mirobod", "Mirzo Ulug'bek", "Shayxontohur", "Uchtepa", "Yashnobod", "Yakkasaray", "Sergeli", "Olmazor"],
        andijan: ["Andijan", "Asaka", "Baliqchi", "Boz", "Jalolquduq", "Izboskan", "Qo'rg'ontepa", "Marhamat", "Oltinko'l"],
        bukhara: ["Bukhara", "G'ijduvon", "Jondor", "Kogon", "Qorako'l", "Qorovulbozor", "Romitan", "Shofirkon", "Vobkent"],
        fergana: ["Fergana", "Qo'qon", "Marg'ilon", "Beshariq", "Buvayda", "Dang'ara", "Furqat", "Oltiariq", "Quva"],
        jizzakh: ["Jizzakh", "Arnasoy", "Baxmal", "G'allaorol", "Sharof Rashidov", "Zafarobod", "Zomin", "Mirzacho'l"],
        khorezm: ["Urganch", "Bog'ot", "Gurlan", "Xonqa", "Shovot", "Tuproqqala", "Yangiariq", "Yangibozor"],
        namangan: ["Namangan", "Chortoq", "Chust", "Kosonsoy", "Mingbuloq", "Norin", "Pop", "To'raqo'rg'on"],
        navoi: ["Navoi", "Karmana", "Qiziltepa", "Xatirchi", "Konimex", "Nurota"],
        qashqadaryo: ["Qarshi", "Dehqonobod", "G'uzor", "Kasbi", "Koson", "Mirishkor", "Muborak", "Nishon", "Shahrisabz", "Yakkabog'"],
        samarkand: ["Samarkand", "Bulung'ur", "Ishtixon", "Jomboy", "Kattaqo'rg'on", "Narpay", "Nurobod", "Oqdaryo", "Paxtachi"],
        sirdaryo: ["Guliston", "Boyovut", "Sayxunobod", "Sardoba", "Shirin", "Xovos"],
        surxondaryo: ["Termiz", "Angor", "Boysun", "Denov", "Jarqo'rg'on", "Muzrabot", "Qiziriq", "Sherobod", "Sho'rchi", "Sariosiyo"],
        karakalpakstan: ["Nukus", "Amudaryo", "Beruniy", "Chimboy", "Ellikqala", "Kegeyli", "Mo'ynoq", "Qonliko'l", "Qo'ng'irot", "Shumanay", "Taxtako'pir", "To'rtko'l", "Xo'jayli"]
    };

    $("#region").change(function() {
        var region = $(this).val();
        var $districtDropdown = $("#district");
        
        $districtDropdown.empty().append('<option value="">District</option>');
        
        if (region && districtOptions[region]) {
            districtOptions[region].forEach(function(district) {
                $districtDropdown.append('<option value="' + district.toLowerCase().replace(/\s/g, '-') + '">' + district + '</option>');
            });
        }
    });
});

$(document).ready(function () {
    let filterSection = $(".search-filter__tools").eq(2);
    let toggleButton = $("#toggle-filter");

    filterSection.hide();

    toggleButton.click(function () {
        filterSection.slideToggle(300, function () { 
            if (filterSection.is(":visible")) {
                toggleButton.html('Close filter <i class="fa-solid fa-angle-up"></i>');
            } else {
                toggleButton.html('View all filter <i class="fa-solid fa-angle-down"></i>');
            }
        });
    });
});


