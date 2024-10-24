  // Fetch team members data from the API
  fetch('/api/team')
  .then(response => response.json())
  .then(data => {
      const teamMembersContainer = document.getElementById('team-members');
      data.forEach(member => {
          const memberSection = `
              <div class="col-md-12">
                  <div class="team-member-section">
                      <img src="${member.image}" alt="${member.name}" class="img-fluid rounded-circle">
                      <h2>${member.name}</h2>
                      <h5>${member.nim}</h5>
                      <h5>${member.education}</h5>
                      <p>${member.bio}</p>
                      <div class="social-links">
                          <a href="${member.instagram}" target="_blank" class="instagram">
                              <i class="fab fa-instagram fa-2x"></i>
                              <span class="instagram-username">@${member.instagram_username}</span>
                          </a>
                      </div>
                  </div>
              </div>
          `;
          teamMembersContainer.innerHTML += memberSection;
      });
  })
  .catch(error => console.error('Error fetching team members:', error));

// <!-- Scroll animation JavaScript -->

// Check if elements are in view
function isInView(element) {
const rect = element.getBoundingClientRect();
return (
  rect.top >= 0 &&
  rect.left >= 0 &&
  rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
  rect.right <= (window.innerWidth || document.documentElement.clientWidth)
);
}

// Add 'in-view' class when the team members are scrolled into view
function checkTeamMembersInView() {
const teamMembers = document.querySelectorAll('.team-member-section');
teamMembers.forEach(member => {
  if (isInView(member)) {
      member.classList.add('in-view');
  }
});
}

// Listen for scroll events
window.addEventListener('scroll', checkTeamMembersInView);
window.addEventListener('load', checkTeamMembersInView);