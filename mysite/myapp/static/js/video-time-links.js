document.addEventListener('DOMContentLoaded', (event) => {
    const videoDescriptions = document.querySelectorAll('[id^="description_"]');

    videoDescriptions.forEach((desc) => {
        const videoId = desc.id.replace('description_', '');
        const videoElement = document.getElementById(`video_${videoId}`);
        const descriptionText = desc.innerHTML;
        const timeLinkRegex = /(\d+):(\d+)/g;
        let updatedDescription = descriptionText.replace(timeLinkRegex, (match, p1, p2) => {
            const seconds = parseInt(p1) * 60 + parseInt(p2);
            return `<a href="#" onclick="document.getElementById('video_${videoId}').currentTime = ${seconds}; return false;">${match}</a>`;
        });
        desc.innerHTML = updatedDescription;
    });
});
