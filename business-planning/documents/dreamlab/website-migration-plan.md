# DreamLab Website Migration Plan
## From Nuclear-Focused to Creative Technology Leadership

### Executive Summary
This plan outlines the migration from the current nuclear-focused dreamlab-website to the production dreamlab-ai-website, repositioning DreamLab as a creative technology and engineering simulation leader while maintaining nuclear sector services as a secondary offering.

## Current State Analysis

### dreamlab-website (To Be Retired)
- **Focus**: 70% nuclear industry, Lake District location
- **Messaging**: Sellafield ecosystem, executive nuclear training
- **Technology**: Basic HTML/CSS/JS with Vite
- **Status**: Incorrect market positioning and location

### dreamlab-ai-website (Production Site)
- **Current State**: Minimal content, just landing page
- **Technology**: React, TypeScript, Tailwind CSS
- **Features**: TorusKnot visualization, email signup
- **Opportunity**: Full rebuild with correct positioning

## Migration Objectives

1. **Reposition** from nuclear-focused to creative technology leader
2. **Showcase** virtual production and engineering simulation capabilities
3. **Maintain** nuclear as one of several market segments (20%)
4. **Highlight** team expertise in creative technology
5. **Create** compelling visual demonstrations of capabilities
6. **Optimize** for creative industry keywords and SEO

## Content Migration Strategy

### Phase 1: Core Content Development (Week 1-2)

#### Homepage Redesign
```typescript
// New hero section focus
{
  headline: "Where Creative Vision Meets Engineering Precision",
  subheadline: "Master virtual production, gaussian splatting, and advanced simulation at the UK's premier residential tech facility",
  cta: ["Explore Creative Programs", "View Our Facilities"]
}
```

#### Service Pages Structure
1. **/virtual-production** - LED volume training, ICVFX workflows
2. **/neural-rendering** - Gaussian splatting, photogrammetry
3. **/engineering-viz** - CAE/CFD visualization, digital twins
4. **/ai-creative** - AI/ML for content creation
5. **/telepresence-xr** - Remote collaboration, holographic tech
6. **/nuclear-energy** - Maintained but de-emphasized

### Phase 2: Visual Content Creation (Week 2-3)

#### Key Visual Assets Needed
1. **Virtual Production Showreel** - LED volume in action
2. **Gaussian Splatting Demo** - Interactive 3D captures
3. **Facility Virtual Tour** - 360° experience
4. **Student Work Gallery** - Portfolio of projects
5. **Technology Demos** - WebGL visualizations

#### Interactive Components
```typescript
// Example: Interactive tech showcase
<TechShowcase>
  <VirtualProductionDemo />
  <GaussianSplattingViewer />
  <EngineeringVizExamples />
  <StudentProjectGallery />
</TechShowcase>
```

### Phase 3: Team & About Section (Week 3)

#### Updated Team Profiles Focus
- **Pete Woodbridge (CTO)**: Emphasize virtual production expertise
- **Ste Moyler (CCO)**: Highlight 25 years in film/animation/VR
- **Dr John O'Hare (CHO)**: Focus on XR and telecollaboration
- **New Additions**: Industry advisors from creative tech

#### About Page Themes
1. Innovation heritage in creative technology
2. Cross-disciplinary approach
3. Sustainable tech practices
4. Industry partnerships and credentials

### Phase 4: Program & Curriculum Pages (Week 4)

#### Program Categories
```typescript
interface ProgramStructure {
  creativeTech: {
    virtualProduction: Course[];
    neuralRendering: Course[];
    aiForCreatives: Course[];
  };
  engineeringViz: {
    simulationViz: Course[];
    digitalTwins: Course[];
  };
  specializedTech: {
    telepresence: Course[];
    droneTech: Course[];
  };
  traditional: {
    nuclearTraining: Course[]; // Maintained but not featured
  };
}
```

## Technical Migration Plan

### Development Approach
1. **Maintain** existing React/TypeScript foundation
2. **Enhance** with Three.js for 3D demonstrations
3. **Add** video streaming for virtual tours
4. **Implement** course booking system
5. **Optimize** for performance and SEO

### Key Features to Implement

#### 1. Dynamic Course Catalog
```typescript
// Course filtering and search
<CourseExplorer
  filters={['technology', 'duration', 'level', 'price']}
  categories={['creative', 'engineering', 'hybrid']}
  sortOptions={['popularity', 'date', 'price']}
/>
```

#### 2. Virtual Facility Tour
```typescript
// 360° tour component
<FacilityTour
  spaces={['vpStage', 'mocapStudio', 'gaussianLab', 'droneZone']}
  interactiveHotspots={true}
  vrEnabled={true}
/>
```

#### 3. Portfolio Showcase
```typescript
// Student and facility work
<PortfolioGallery
  categories={['virtualProduction', 'neuralRendering', 'simulation']}
  mediaTypes={['video', 'interactive3D', 'beforeAfter']}
/>
```

## SEO & Marketing Optimization

### Target Keywords (Primary)
- "virtual production training UK"
- "gaussian splatting course"
- "LED volume training"
- "engineering visualization training"
- "telepresence development course"

### Content Strategy
1. **Blog Topics**: Technical tutorials, industry insights
2. **Case Studies**: Success stories from each sector
3. **Resource Library**: Free guides and tools
4. **Video Content**: YouTube channel integration

## Migration Timeline

### Week 1-2: Foundation
- [ ] Finalize site architecture
- [ ] Create content templates
- [ ] Develop core pages
- [ ] Set up CMS structure

### Week 3-4: Content Creation
- [ ] Write all service pages
- [ ] Create visual assets
- [ ] Develop interactive demos
- [ ] Update team profiles

### Week 5-6: Development
- [ ] Implement new features
- [ ] Integrate booking system
- [ ] Add interactive components
- [ ] Optimize performance

### Week 7-8: Testing & Launch
- [ ] User testing with target audiences
- [ ] SEO optimization
- [ ] Performance testing
- [ ] Soft launch to select partners
- [ ] Full public launch

## Success Metrics

### Primary KPIs
- **Traffic Split**: 50% creative, 20% engineering, 20% nuclear, 10% other
- **Conversion Rate**: 3-5% visitor to inquiry
- **Engagement**: 3+ minutes average session
- **SEO Rankings**: Top 10 for primary keywords

### Secondary Metrics
- Portfolio views and interactions
- Video engagement rates
- Course page dwell time
- Mobile vs desktop usage
- Geographic distribution

## Risk Mitigation

1. **SEO Impact**: 301 redirects from old site
2. **Brand Confusion**: Clear messaging about evolution
3. **Nuclear Clients**: Dedicated portal maintained
4. **Technical Issues**: Staged rollout with fallback

## Post-Launch Plan

### Month 1
- Monitor analytics and user feedback
- A/B test key conversion pages
- Refine based on data
- Launch paid marketing campaigns

### Month 2-3
- Expand content library
- Add customer testimonials
- Implement chat support
- Launch email nurture campaigns

### Ongoing
- Monthly content updates
- Seasonal program launches
- Partnership announcements
- Technology showcase updates

## Budget Estimate

| Item | Cost |
|------|------|
| Content Creation | £5,000 |
| Visual Assets | £8,000 |
| Development | £12,000 |
| SEO/Marketing | £5,000 |
| **Total** | **£30,000** |

## Conclusion

This migration represents a critical repositioning of DreamLab from regional nuclear training to national creative technology leadership. By maintaining nuclear as a segment while expanding into high-growth creative markets, we can achieve the £3M revenue target by Year 3.

The new website will serve as the primary conversion tool for this transformation, showcasing our unique position at the intersection of creative vision and engineering precision.