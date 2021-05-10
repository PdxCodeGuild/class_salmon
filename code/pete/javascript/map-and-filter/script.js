const heroesAndVillains = [
  { name: 'Joker', location: 'Gotham City', role: 'villain' },
  { name: 'Penguin', location: 'Gotham City', role: 'villain' },
  { name: 'Superman', location: 'Metropolis', role: 'hero' },
  { name: 'The Flash', location: 'Central City', role: 'hero' },
  { name: 'Killer Croc', location: 'Gotham City', role: 'villain' },
  { name: 'Robin', location: 'Gotham City', role: 'hero' },
  { name: 'Catwoman', location: 'Gotham City', role: 'hero' }
]

// const heroes = heroesAndVillains.filter(heroOrVillain => heroOrVillain.role === 'hero')
// console.log(heroes)

// const villains = heroesAndVillains.filter(heroOrVillain => heroOrVillain.role === 'villain')
// console.log(villains)

// function makeInvite (attendee) {
//   return `Dear ${attendee.name} in ${attendee.location}.  You are invited to a reunion meetup.  PM me for Zoom link.`
// }

// const invites = heroesAndVillains.map(makeInvite)
// console.log(invites)

// const heroInvites = heroesAndVillains.filter(heroOrVillain => heroOrVillain.role === 'hero').map(makeInvite)
// const villainInvites = heroesAndVillains.filter(heroOrVillain => heroOrVillain.role === 'villain').map(makeInvite)

// console.log(heroInvites, villainInvites)

function reducer (accumulator, heroOrVillain) {
  if (heroOrVillain.role === 'hero') {
    accumulator.heroes.push(heroOrVillain)
  } else if (heroOrVillain.role === 'villain') {
    accumulator.villains.push(heroOrVillain)
  }
  return accumulator
}

const reorganizedHeroesAndVillains = heroesAndVillains.reduce(reducer, { heroes: [], villains: [] })
console.log(reorganizedHeroesAndVillains)
// newVersion = {
//   heroes: [],
//   villains: []
// }
