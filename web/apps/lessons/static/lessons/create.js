document.addEventListener('DOMContentLoaded', function () {
    const typeSelect = document.querySelector('select[name="typ"]');
    const divVideo = document.getElementById('div_video');
    const divPres = document.getElementById('div_presentation');
    const divDoc = document.getElementById('div_document');

    function toggleFields() {
        const value = typeSelect.value;

        divVideo.style.display = 'none';
        divPres.style.display = 'none';
        divDoc.style.display = 'none';

        if (value === 'video') divVideo.style.display = 'block';
        if (value === 'presentation') divPres.style.display = 'block';
        if (value === 'document') divDoc.style.display = 'block';
    }

    typeSelect.addEventListener('change', toggleFields);
    toggleFields();
});
