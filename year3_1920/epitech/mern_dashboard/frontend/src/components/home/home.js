import React from 'react';
import GridLayout from 'react-grid-layout';
import UserTweets from '../widgets/twitter/userTweets';


class Home extends React.Component {

    render() {
        return (
            <div className="Home-dashboard">
                {/* <ul className="Home-actions">
                    <li>+</li>
                    <li>O</li>
                </ul> */}
                <GridLayout className="Home-gridLayout" 
                    cols={16} rowHeight={30} width={1200} 
                    verticalCompact={false} >
                    <div key="a" data-grid={{x: 5, y: 0, w: 1, h: 1}}>
                        <div className="Home-widget">
                            <UserTweets />
                        </div>
                    </div>
                    {/* <div key="b" data-grid={{x: 12, y: 0, w: 1, h: 1}}>
                        <div className="Home-widget">
                            <UserTweets />
                        </div>
                    </div> */}
                </GridLayout>
            </div>
        );
    }
}


export default Home;